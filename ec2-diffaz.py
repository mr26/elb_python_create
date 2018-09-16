#!/usr/bin/python

import boto3


ec2 = boto3.resource('ec2')

instance = ec2.create_instances(

        ImageId='ami-01399f850445996a3',
        InstanceType='t2.micro',
        KeyName='py-key-pair',
        MaxCount=1,
        MinCount=1,
        Monitoring={ 'Enabled': True },

        Placement={
                'AvailabilityZone': 'us-east-1c',
                },

        SecurityGroups=['sec-grp3'],

        TagSpecifications=[
                {
                        'ResourceType': 'instance',
                        'Tags': [
                           {
                                'Key': 'infra',
                                'Value': 'Apache Group'
                           },
                ]
         },
        ],


        )




#ami-01399f850445996a3
