import requests
import argparse

from flask import Flask, redirect, render_template, request, json, jsonify
from pprint import pprint

import jenkins_utils

app = Flask(__name__)
VERSION = 0.2

@app.route('/jobs')
def jobs():
    return jsonify(jenkins_utils.all_jobs(url))


@app.route('/job/<job_name>')
def job(job_name):
    return jsonify(jenkins_utils.job_builds(url, job_namejob_name))

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
