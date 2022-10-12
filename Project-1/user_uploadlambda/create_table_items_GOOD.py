#this program is for creating a table in mysql and 


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

    name="joe"
    employeeid=1
    today=date.today()
    
    with conn.cursor() as cur:
        cur.execute("create table Apptable ( UserID  int NOT NULL, Name varchar(255) NOT NULL, input_date DATE, PRIMARY KEY (EmpID))")
        cur.execute('insert into Apptable (UserID, Name, input_date) values(%s, %s, %s)', (employeeid, name, today))
        conn.commit()
        cur.execute("select * from Apptable")
        for row in cur:
            logger.info(row)
            print(row)
    conn.commit()