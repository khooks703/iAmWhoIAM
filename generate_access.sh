#!/bin/bash
arn=$1
days=$2

jobId=$(aws iam  generate-service-last-accessed-details --granularity ACTION_LEVEL --arn $arn --query JobId | tr -d '"')

job_details=$(aws iam get-service-last-accessed-details --job-id $jobId --query ServicesLastAccessed)

$job_details > access_details.json

python make_policy.py $days