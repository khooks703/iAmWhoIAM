#!/bin/bash
arn=$1
days=$2

if test -f "policy_document.json"; then
  rm policy_document.json
fi

if test -f "removed_policies_document.json"; then
  rm removed_policies_document.json
fi
jobId=$(aws iam  generate-service-last-accessed-details --granularity ACTION_LEVEL --arn $arn --query JobId | tr -d '"')

aws iam get-service-last-accessed-details --job-id $jobId --query ServicesLastAccessed > access_details.json

python create_policy.py $days