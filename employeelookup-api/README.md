# Sample Employee Lookup API
Uses serverless framework to deploy the flask application which talks to Dynamodb employee table to GET and POST data. 

## How to setup the app
Made modifications from an existing [sample app](https://serverless.com/learn/tutorials/flask-rest-api-serverless/).

## Steps Involved
1. Setup [AWS Credentials for Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/credentials/) <br>

2. Installation of npm serverless
```
npm install -g serverless
```

3. Install a few dependencies. We're going to use the serverless-wsgi plugin for negotiating the API Gateway event type into the WSGI format that Flask expects. We'll also use the serverless-python-requirements plugin for handling our Python packages on deployment. 
```
npm install --save-dev serverless-wsgi serverless-python-requirements
```
Note: Make sure you have [docker installed](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) on your host and docker deamon is accessible by the user running the deployment.

4. Create a virtual environment and activate it
```
virtualenv venv --python=python3
source venv/bin/activate
```

5. Install the Flask and boto3 package with pip, and save your dependencies in requirements.txt
```
(venv) $ pip install flask boto3
(venv) $ pip freeze > requirements.txt
```

6. To deploy api
```
(venv) ubuntu@nordstrom:~/work/api$ sls deploy
Serverless: Installing required Python packages with python3.6...
Serverless: Docker Image: lambci/lambda:build-python3.6
Serverless: Linking required Python packages...
Serverless: Packaging Python WSGI handler...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Unlinking required Python packages...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
.....
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (25.97 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
....................................
Serverless: Stack update finished...
Service Information
service: serverless-flask
stage: dev
region: us-east-1
stack: serverless-flask-dev
api keys:
  None
endpoints:
  ANY - https://2qhmhgtzmj.execute-api.us-east-1.amazonaws.com/dev
  ANY - https://2qhmhgtzmj.execute-api.us-east-1.amazonaws.com/dev/{proxy+}
functions:
  app: serverless-flask-dev-app
```
<br>

## To Test the app is working
```
export BASE_DOMAIN=https://2qhmhgtzmj.execute-api.us-east-1.amazonaws.com/dev
curl -X get ${BASE_DOMAIN}
```
On success you should get a Hello World!

## To POST new employeeIds
```
curl -H "Content-Type: application/json" -X POST ${BASE_DOMAIN}/employees -d '{"employeeId": "470419", "name": "Mithun Cheriyath"}'
```

## To GET employeeIds
```
curl -H "Content-Type: application/json" -X GET ${BASE_DOMAIN}/employees/470419
```

