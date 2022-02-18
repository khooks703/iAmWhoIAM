# iAmWhoIAM
IAM Policy Cleaner
## Description
A simple way to generate an iam policy statement to use the least privilege up to the action level.

## Requirements
* aws cli
    - access to iam permissions:
        ```
        iam:GenerateServiceLastAccessedDetails
        iam:GetServiceLastAccessedDetails
        iam:list*
        ```
* python 3
    - if python 3 is not your default python use a virtual environment:
        ```
        python3 -m venv venv
        . venv/bin/activate
        ```
## Run Script
```
chmod +x run.sh
./run.sh iam-arn [expire-days]
```
* `iam-arn`(string) Required. Arn of an iam user/group/role/policy
* `expire-days`(integer) Optional. Number of days from when the service was last accessed before removing it from the policy document. Services removed this way will be put into a separate policy document `out/removed_policies_document.json`

### Example Use Cases
* Clean up existing iam roles that are too permissive
* Run the script against an iam user arn and number of days to list all the services/actions used within that amount of days in order to rid unused permissions
* When creating a new pipeline to deploy an application a developer could give it a permissive role until the pipeline is in a working state, then run this script and pass in the role arn in order to generate a policy document that will list all the services/actions that were used in the pipeline.
