import json 
import sys
from datetime import datetime

try:
    input_days=int(sys.argv[1])
except IndexError:
    input_days=99999
date_format_str = '%Y-%m-%d'

date_now = datetime.now()
date_now = f"{date_now.strftime('%Y')}-{date_now.strftime('%m')}-{date_now.strftime('%d')}"
fileObject=open("access_details.json", "r")
jsonContent=fileObject.read()
data=json.loads(jsonContent)

statements=[]
for i in data:
    service=i['ServiceNamespace']
    last_date=i['LastAuthenticated'].split("T")[0]

    start = datetime.strptime(str(date_now), date_format_str)
    end = datetime.strptime(str(last_date), date_format_str)
    days = start - end
    
    actionList=[]
    if "TrackedActionsLastAccessed" in i:
        actions=i['TrackedActionsLastAccessed']
        actionList=[]
        for i in actions:
            action=f"{service}:{i['ActionName']}"
            actionList.append(action)
    else:
        actionList.append(f"{service}:*")

    statement={
        "Effect":"Allow",
        "Action":actionList,
        "Resource":["*"]
    }
    if input_days > int(days.days):
        statements.append(statement)
policy={
    "Version":"2012-10-17",
    "Statement":statements
}

policyJson=json.dumps(policy, indent=4)
with open("policy_document.json", "w") as outfile:
    outfile.write(policyJson)
print("Policy Created: policy_document.json")
