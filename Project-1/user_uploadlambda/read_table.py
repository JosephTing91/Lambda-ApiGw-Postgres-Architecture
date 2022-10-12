import json
import pymysql
import boto3
import logging
import sys
from datetime import date

logger = logging.getLogger()
logger.setLevel(logging.INFO)

rds_host='terraform-20221012153942984900000003.cggdpmo6alkj.us-east-1.rds.amazonaws.com'
name='joseph'
password='ting1234'
db_name='mydb'
today=date.today()

conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=20)

def lambda_handler(event, context):
    with conn.cursor() as cur:
        cur.execute("select * from Employee3")
        rows=cur.fetchall()
        for row in rows:
            print(row)
    conn.commit()





        cur.execute("create table Employee5 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, input_date DATE, PRIMARY KEY (EmpID))")