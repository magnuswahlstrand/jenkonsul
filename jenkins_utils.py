import requests

# Custom function to find tracks in your CI. Replace with your own
def find_tracks(jenkins_url):
    path = "api/json?tree=jobs[name]&pretty=true"
    response = requests.get(jenkins_url + path)
    return [job.split('.')[1] for job in [job['name'] for job in response.json()['jobs'] if job['name'].endswith('deployment-vm.test')]][::-1]
