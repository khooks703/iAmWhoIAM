#!/bin/bash
arn=$1
days=$2

jobId=$(aws iam  generate-service-last-accessed-details --granularity ACTION_LEVEL --arn $arn --query JobId | tr -d '"')

aws iam get-service-last-accessed-details --job-id $jobId --query ServicesLastAccessed > access_details.json

python create_policy.py $days