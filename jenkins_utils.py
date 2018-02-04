import requests
import json

# Custom function to find tracks in your CI. Replace with your own
def find_tracks(jenkins_url):
    path = "api/json?tree=jobs[name]&pretty=true"
    response = requests.get(jenkins_url + path)
    return [job.split('.')[1] for job in [job['name'] for job in response.json()['jobs'] if job['name'].endswith('deployment-vm.test')]][::-1]

def find_jobs_and_tracks(jenkins_url, job_name):
    return [{'track': track, 'job_name': job_name.format(track=track)} for track in find_tracks(jenkins_url)]


# Splits time into a more managable formats. Returns a dict
def format_time(duration):

    time = {}
    time['seconds_total'] = int(duration/1000)
    time['minutes'] = int(time['seconds_total']/60)
    time['seconds'] = time['seconds_total'] - 60*time['minutes']
    return time

# Restructures the build information to a format suitable for datatables consumption
def build_to_datatables_format(job):

    # Turn duration into seconds
    job['duration'] = format_time(job['duration'])

    # Default values
    job['claim'] = None
    job['trigger'] = None

    # Update claim and trigger info
    if 'actions' in job:
        for action in job['actions']:
            if 'claimed' in action and action['claimed'] == True:
                print(action)
                job['claim'] = action['claimedBy'] + ": " + action['reason']

            if 'causes' in action:
                job['trigger'] = action['causes'][0]['shortDescription']

        # Remove from dict
        job.pop('actions')

    return job

def all_jobs(url):
    query_url = "{url}/api/json?tree=jobs[name]&pretty=true".format(url=url)
    response = requests.get(query_url)
    return response.json()

def job_builds(url, job_name):
    query_url = "{url}/job/{job_name}/api/json?tree=allBuilds[id,building,duration,id,result,url,description,actions[claimed,claimedBy,reason,causes[shortDescription]]]&pretty=true".format(url=url, job_name=job_name)
    response = requests.get(query_url)
    data = [build_to_datatables_format(build_data) for build_data in response.json()["allBuilds"] ]
    return data
