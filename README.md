# iAmWhoIAM
IAM Least Privilege Policy Statement Creator
## Description
A simple way to generate an iam policy statement to use the least privilege down to the action level.

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
Example:
`./run.sh arn:aws:iam::123456789012:user/intern 90`
* `iam-arn`(string) Required. Arn of an iam user/group/role/policy
* `expire-days`(integer) Optional. Number of days from when the service was last accessed before removing it from the policy document. Default 365.
## Output
- Creates a policy document as an `out/policy_document.json` file.
- Policies that are removed by `expire-days` will be listed as a policy document as an `out/removed_policies_document.json` file.

### Example Use Cases
* Clean up existing iam roles that are too permissive
* Run the script with an iam user arn and number of days to list all the services/actions used within that amount of days in order to rid unused permissions
* Create a new pipeline to deploy an application with a permissive role until the pipeline is in a working state, 
then run this script with the role arn to generate a policy document that will list all the services/actions that were used in the pipeline.
