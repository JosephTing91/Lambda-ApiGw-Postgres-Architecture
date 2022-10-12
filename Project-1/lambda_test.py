import json
import pymysql
import boto3

rds_host='terraform-20221012055422818300000001.cggdpmo6alkj.us-east-1.rds.amazonaws.com'
name='joseph'
password='ting1234'
db_name='mydb'


conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)


def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
