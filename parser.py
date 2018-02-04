import requests
import argparse

from flask import Flask, redirect, render_template, request, json, jsonify
from pprint import pprint

import jenkins_utils

app = Flask(__name__)
VERSION = 0.2


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


@app.route('/tracks')
def tracks():
    return jsonify(jenkins_utils.find_tracks(url))


@app.route('/')
def home():
    return render_template('index.html', tracks=jenkins_utils.find_tracks(url))

@app.route('/jenkins_data')
def jenkins():
    data = [restructure_response(job_data) for job_data in response.json()["allBuilds"] ]
    return json.jsonify(data)


if __name__ == '__main__':

    parser = argparse.ArgumentParser('Web app that monitors the status of a job in a Jenkins instance')
    parser.add_argument('-u', '--url', required=True, help='the url of the Jenkins instance monitor. Example: http://localhost:8080/jenkins/')

    args = parser.parse_args()
    url = args.url
    print(url)

    app.run(debug=True)
