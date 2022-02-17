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
file_object=open("access_details.json", "r")
json_content=file_object.read()
data=json.loads(json_content)

statements=[]
removed_statements=[]

for i in data:
    service=i['ServiceNamespace']
    last_date=i['LastAuthenticated'].split("T")[0]

    start = datetime.strptime(str(date_now), date_format_str)
    end = datetime.strptime(str(last_date), date_format_str)
    days = start - end
    
    action_list=[]
    if "TrackedActionsLastAccessed" in i:
        actions=i['TrackedActionsLastAccessed']
        action_list=[]
        for i in actions:
            action=f"{service}:{i['ActionName']}"
            action_list.append(action)
    else:
        action_list.append(f"{service}:*")

    statement={
        "Effect":"Allow",
        "Action":action_list,
        "Resource":["*"]
    }
    if input_days > int(days.days):
        statements.append(statement)
    else:
        removed_statements.append(statement)
        
policy={
    "Version":"2012-10-17",
    "Statement":statements
}

policy_json=json.dumps(policy, indent=4)
with open("policy_document.json", "w") as outfile:
    outfile.write(policy_json)
print("Policy Created: policy_document.json")

if removed_statements:
    removed_policy={
        "Version":"2012-10-17",
        "Statement":removed_statements
    }
    removed_policy_json=json.dumps(removed_policy, indent=4)
    with open("removed_policies_document.json", "w") as outfile:
        outfile.write(removed_policy_json)
    print("Policy Created: removed_policies_document.json")