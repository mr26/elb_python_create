#!/usr/bin/python

import boto3
import subprocess
import time

elb = boto3.client('elbv2')

my_lb = elb.create_load_balancer(
	Name='boto-lb',
#	SecurityGroups=['sg-0d49ff619fed13297'],
	Scheme='internet-facing',
	IpAddressType='ipv4',
	Subnets=['subnet-23b9f369','subnet-d47dc7b3'],
	Type='network',
	)
	


my_tg = elb.create_target_group(
	Name='lab-tg',
	Protocol='TCP',
	Port=80,
	TargetType='instance',
	VpcId='vpc-fec81e84')

time.sleep(15)

new_target = subprocess.check_output('aws elbv2 describe-target-groups --name lab-tg --query TargetGroups[*].[TargetGroupArn] --output text', shell=True).strip()

register_targs = elb.register_targets(
		 TargetGroupArn= new_target,
		 Targets=[
		{ 'Id': 'i-0294bf7a5c1eb2707',
		  'Port': 80,
		   },
		{ 'Id': 'i-07114e802c9bda161',
		  'Port': 80,
		  }, ] )


new_lb = subprocess.check_output("aws elbv2 describe-load-balancers --query LoadBalancers[*].[LoadBalancerArn] --output text", shell=True).strip()


lb_listener = elb.create_listener(
	
		LoadBalancerArn=new_lb,
		Protocol='TCP',
		Port=80,
		DefaultActions=[ 
		{
		'Type': 'forward',
		'TargetGroupArn': new_target }, ]
		) 






















