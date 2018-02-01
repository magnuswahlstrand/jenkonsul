import requests
from flask import Flask, redirect, render_template, request, json
from pprint import pprint

app = Flask(__name__)
VERSION = 0.1

url = "http://localhost:8080/job/key-value-adder/api/json?tree=allBuilds[id,building,duration,id,result,url,description,actions[claimed,claimedBy,reason,causes[shortDescription]]]&pretty=true"
response = requests.get(url)


def restructure_response(job):


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

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/jenkins_data')
def jenkins():
    data = [restructure_response(job_data) for job_data in response.json()["allBuilds"] ]
    return json.jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

