#this program is for creating a table in mysql and 
import json
import pymysql
import boto3
import logging
import sys
from datetime import date

logger = logging.getLogger()
logger.setLevel(logging.INFO)


ssm=boto3.client('ssm', 'us-east-1')

password = ssm.get_parameter(
    Name='db_password',
    WithDecryption=True
)['Parameter']['Value']

name=ssm.get_parameter(
    Name='db_username',
    WithDecryption=True
)['Parameter']['Value']

rds_host=ssm.get_parameter(
    Name='db_endpoint',
    WithDecryption=True
)['Parameter']['Value']

db_name='mydb'
today=date.today()


conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=20)

def lambda_handler(event, context):
    name="joe"
    userid=11989
    today=date.today()
    
    with conn.cursor() as cur:

        cur.execute('insert into Apptable (UserID, Name, input_date) values(%s, %s, %s)', (userid, name, today))
        conn.commit()
        cur.execute("select * from Apptable")
        for row in cur:
            logger.info(row)
            print(row)
    conn.commit()
