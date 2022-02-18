# iAmWhoIAM
IAM Policy Cleaner
## Requirements
* aws cli
    - user should have access to iam permissions:
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
* `iam-arn`(string) Required. Is the arn of an iam user/group/role/policy
* `expire-days`(integer) Optional. Is the number of days from when the service was last accessed before removing it from the policy.