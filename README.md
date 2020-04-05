# Profiles Api
Simple HTTP service to work with Twitter profiles powered by Flask.

![twitter-api-demo](https://user-images.githubusercontent.com/23407924/78502536-4a006500-776a-11ea-9c44-4a71ebebc5cb.gif)

## Prerequisites
* Python 3.6+
* Activated new virtual environment
* Git

## Installation
* Clone repository `https://github.com/vladbagmet/profiles_api`
* `cd profiles_api`
* Install external dependencies `pip install -r requirements.txt`

## Launching Service
* Specify Flask app path `export FLASK_APP=handlers/web.py:app`
* Launch HTTP server `flask run`

At this point server should be available by url `http://127.0.0.1:5000/`

## Working with Service
Before sending any HTTP requests, please make sure set `Content-Type: application/json`.
* To retrieve stored profiles `curl -i -H "Content-Type: application/json" http://127.0.0.1:5000/users/`
* To retrieve profile for specific stored user `curl -i -H "Content-Type: application/json" http://127.0.0.1:5000/user/{{handle}}/profile_pic`
Replace `{{handle}}` with twitter profile.
* To request adding data for user whose data was not saved to storage yet `curl -d '{"handle": "{{handle}}"}' -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/scrape/`
Replace `{{handle}}` with twitter profile.

## Before Moving to Production
Let's make an assumption that we plan to run the service on AWS.
* File system storage should be replaced with S3 bucket or DB.
* Async job scheduling should be replaced with SQS queues handling workloads or async Lambda functions calls. 
Alternatively, we can use some async Python framework to work with async content parser.
