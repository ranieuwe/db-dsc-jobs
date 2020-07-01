import json, socket, requests, sys
import auth

from jinja2 import Environment, PackageLoader
from datetime import datetime


current_time = datetime.now().strftime("%H:%M:%S")

# Optional: lift to env files. 
configuration = json.load(open(sys.argv[1]))

auth_token = auth.get_auth_token_from_cert(configuration)

# Settings for jinja2
tplenv = Environment(loader=PackageLoader('job','templates'))
tplenv.filters['jsonify'] = json.dumps

# Settings for request/urllib3
head = {'Authorization': 'Bearer ' + auth_token["access_token"], 'Content-Type': 'application/json'}

# Get something from Databricks, parse to JSON if asked
def get_db(action, returnJson=False):
    url = databricks_uri % action
    log("REST - GET - Calling %s" % action)
    response = requests.get(url, headers=head)
    return response.json() if json else response

# Post something from Databricks, parse to JSON if asked
def post_db(action, jsonpl, returnJson=False):
    url = databricks_uri % action
    log("REST - POST - Calling %s" % action)
    response = requests.post(url, headers=head, data=jsonpl)
    return response

# Delete a job, this is a guaranteed operation by the Databricks API on successful ack.
def delete_job(id):
    log("Deleting %s" % id)

    tpl = tplenv.get_template('delete.jinja2').render(id=id)
    result = post_db("jobs/delete", tpl)
    if(result.ok):
        log("Deleted job %s" % id)
    else:
        log("Error deleting job: %s" % result.content)

# Helper to print timestamps
def log(s):
    print("[%s] %s" % (current_time, s))

def main():

    log("Running execution against %s" % databricks_uri.split('/')[2])

    jobs = get_db("jobs/list", returnJson=True)
    jobnames = []

    if(len(jobs) > 0): 
        log("Total of %s jobs found" % len(jobs['jobs']))
        jobnames = [(j['settings']['name'],j['job_id']) for j in jobs['jobs']]
    else:
        log("No jobs")

    # Set up definition based on input from Molly
    job1 = {
        'name': 'Jinja job example',
        'workers': 10,
        'description': 'Not used in template, for reference'
    }

    # Delete active jobs for the name in job1
    # TODO: The above definition need to come from a folder in DBFS, then loop over them and pull. 
    [delete_job(item[1]) for item in jobnames if item[0] == job1['name']]
    
    # Create a new job with the name above
    template = tplenv.get_template('standard.jinja2')
    task = template.render(job=job1)
    
    result = post_db("jobs/create", task).json()
    log("Created a new job %s" % result['job_id'])

# Module hook
if __name__ == '__main__':
    main()