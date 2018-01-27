# Jenkonsul
A guide how to set up a simple Jenkins/Consul system using dockers and jenkins job results to it.

## Setup environment

### Start Jenkins
1. Start Jenkins in docker
```
docker run --name jenkonsul -p 8080:8080 jenkinsci/blueocean
```

### Start consul
```
docker run --name konsul -p 8500:8500 -p 8600:8600 consul
```

### Setup jenkins
1. Go to http://localhost:8080, enter password found in the terminal from step 
3. Follow the wizard to setup your Jenkins. Default values is fine.

### Setup `Consul KV builder` plugin
1. Go to [plugin manager](http://localhost:8080/pluginManager/available) (localhost:8080 --> Manage Jenkins --> Manage Plugins --> Available)
2. Search for Consul
4. Install the [Consul KV builder](https://wiki.jenkins.io/display/JENKINS/Consul-KV-Builder+Plugin) plugin
5. Go to Jenkins [configuration page](http://localhost:8080/configure), and configure to match your consul. Ip address should to be the host ip
![alt text](jenkins_plugin_settings.png "Example configuration" )

### Setup Jenkins jobs
1. Create a regular Jenkins jobs
2. Add Consul build steps
![alt text](jenkins_build_step.png "Example configuration" )
3. Run the job
4. Check the results http://localhost:8500/ui/#/dc1/kv


# Using Jenkins REST directly.
Sometimes, using the native REST api can give you the same results. 

Example: http://localhost:8080/api/json?tree=jobs[name]&pretty=true

| URL <br>[localhost:8080/](http://localhost:8080/)        | Tree           |Description|
| ------------- |:-------------|:-------------|
| api/json | ?tree=jobs[name]&pretty=true | Name of all defined jobs |
| job/<JOB_NAME>/api/json | ?tree=allBuilds[id]&pretty=true | The IDs of all builds of JOB_NAME |
| job/<JOB_NAME>/api/json | ?tree=allBuilds[id]{0,2}&pretty=true | The IDs of the last 2 builds |
| job/<JOB_NAME>/api/json | ?depth=1&pretty=true | All metadata, depth=2. <br>Increase depth for more info |
| job/<JOB_NAME>/api/json | ?tree=allBuilds[id,url,result,duration] | ID, url, result and duration. <br>More options in line above |
|  job/<JOB_NAME>/api/json |?tree=allBuilds[id,actions[causes[shortDescription]]{0}]| Show who/what started build  |
| | | |

[Jenkins guide](http://localhost:8080/api/)
[How to use the API](https://www.cloudbees.com/blog/taming-jenkins-json-api-depth-and-tree)