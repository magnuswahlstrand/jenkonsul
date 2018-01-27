

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
4. Check the results http://localhost:8500/ui/#/dc1/kv# jenkonsul
