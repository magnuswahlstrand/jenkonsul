import requests
import argparse
import sys

from flask import Flask, redirect, render_template, request, json, jsonify

import jenkins_utils

app = Flask(__name__)
VERSION = 0.2

# Util function to simplify troubleshooting
@app.route('/tracks')
def tracks():
    return jsonify(jenkins_utils.find_tracks(url))

# Util function to simplify troubleshooting
@app.route('/jobs_and_tracks')
def jobs_and_tracks():
    return jsonify(jenkins_utils.find_jobs_and_tracks(url, job_name))


@app.route('/jobs')
def jobs():
    return jsonify(jenkins_utils.all_jobs(url))


@app.route('/job/<job_name>')
def job(job_name):
    return jsonify(jenkins_utils.job_builds(url, job_name))


@app.route('/')
def home():
    return render_template('index.html', jobs=jenkins_utils.find_jobs_and_tracks(url, job_name))

@app.route('/jenkins_data')
def jenkins():
    data = [restructure_response(job_data) for job_data in response.json()["allBuilds"] ]
    return json.jsonify(data)


if __name__ == '__main__':

    parser = argparse.ArgumentParser('Web app that monitors the status of a job in a Jenkins instance')
    parser.add_argument('-u', '--url', required=True, help='the url of the Jenkins instance monitor. Example: http://localhost:8080/jenkins/')
    parser.add_argument('-j', '--job-name', required=True, help='The monitored job, with variable track name. "{track}" will be replaced for each track. Example: "basename.{track}.deployment-test')


    args = parser.parse_args()
    url = args.url
    job_name = args.job_name

    if "{track}" not in job_name:
        print("\nERROR: --job-name must contain \"{track}\"")
        sys.exit(1)

    app.run(debug=True, host='0.0.0.0')
