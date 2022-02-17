#!/bin/bash
arn=$1
days=$2

if [ -f "out/policy_document.json" ] ; then
  rm out/policy_document.json
fi

if [ -f "out/removed_policies_document.json" ] ; then
  rm out/removed_policies_document.json
fi

if [ -f "access_details.json" ] ; then
  rm access_details.json
fi

jobId=$(aws iam  generate-service-last-accessed-details --granularity ACTION_LEVEL --arn $arn --query JobId | tr -d '"')
sleep 2
aws iam get-service-last-accessed-details --job-id $jobId --query ServicesLastAccessed > access_details.json

python create_policy.py $days
