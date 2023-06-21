
import requests 
import json

jira_url = "jira-api-endpoint"

username = "abcd"
api_token = "abcg@e"

project_key = "project_key"
issue_type = "task"
summary = "summary of the issue to be created"
description = "the issue wa created automatically using a script"

payload = {
   "fields" : {
       "project": {
          "key" : project_key
   },
        "summary": summary,
        "description": description,
        "issuetype":{
           "name": issue_type
    }
    }
}
response = requests.post(
       auth = (username, api_token),
       headers = {"Content-Type": "application/json"}
)

if response.status_code == 201:
    print("issue created successfully")
    issue_key = response.json()["key"]
    url = jira_url + "/browse" + issue_type
    print("issue link:", {url})
else:
    print("failed to create the issue.Status code,", response.status_code)
    print("response:", response.text)