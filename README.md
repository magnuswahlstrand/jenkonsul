# Jenkonsul

A web app that monitors Jenkins jobs. Not using Consul anymore :-).


## Docker

#### Build
```bash
docker build -t jenkonsul .
```

#### Run
```bash
docker run -i -t --rm jenkonsul -p 5050:5000 -u http://localhost:8080/jenkins/ -j "basename.{track}.deployment-test"
```

## Releases

### Upcoming

#### 0.5
2. Break out header for table to separate definition
2. Add variable for port

#### 0.x
5. Add picture of working app
1. Add config file
4. Refresh table on change of tab
3. Add Help page
3. Add mail feedback mechanism

1. Show git push triggering
2. git: link to triggering commit

#### 0.errorhandling
4. Error handling: no jenkins
4. Error handling: no tracks
4. Error handling: no jobs

### Done

#### ~0.4~
3. ~Include claim information~
1. ~Add gitignore~
3. ~Create docker file for file~
4. ~Pass all arguments to docker command~
4. ~Separate file for js-callbacks~
5. ~Link to claim page~

#### ~0.3~
1. ~Colors for row or column based on result~
2. ~Automatic refresh of current page~

1. ~One datatable per table tab~
4. ~URL to job~
5. ~Duration in seconds~

#### ~0.2~
1. ~First working version. Showing ID, Duration and Result of a jenkins job~

## Links
```
{{jenkins_url}}/job/{{job_name}}
{{jenkins_url}}/job/{{job_name}}
/job/{{job_name}}
{{jenkins_url}}/job/{{job_name}}/api/json?depth=3&pretty=true
{{jenkins_url}}/job/{{job_name}}/api/json?tree=allBuilds[id,building,duration,id,result,url,description,actions[assignedBy,claimed,claimedBy,reason,causes[shortDescription],foundFailureCauses[categories,description,id,name]]]&pretty=true
```
