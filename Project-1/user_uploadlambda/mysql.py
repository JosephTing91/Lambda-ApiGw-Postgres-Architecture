

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

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """

    item_count = 0
    with conn.cursor() as cur:
         cur.execute("create table Employee2 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, input_day DATE NOT NULL,PRIMARY KEY (EmpID))")
         cur.execute('insert into Employee2 (EmpID, Name, input_day) values(1, "Joe", today)')
         cur.execute('insert into Employee2 (EmpID, Name, input_day) values(2, "Bob", today)')
         cur.execute('insert into Employee2 (EmpID, Name, input_day) values(3, "Mary", today)')
         conn.commit()
         cur.execute("select * from Employee2")
         for row in cur:
                item_count += 1
                logger.info(row)
                   #print(row)
    conn.commit()

    return "Added %d items from RDS MySQL table" %(item_count)








import json
import pymysql
rds_host='terraform-20221012153942984900000003.cggdpmo6alkj.us-east-1.rds.amazonaws.com'
name = 'joseph'
password = 'ting1234'
db_name = 'mydb'
port = 3306

try:
    conn = pymysql.connect(host=rds_host,user=name,
                           passwd=password,db=db_name,
                           connect_timeout=5,
                           cursorclass=pymysql.cursors.DictCursor)
except:
    sys.exit()
def lambda_handler(event, context):
    with conn.cursor() as cur:
        qry = "select * from playlist"
        cur.execute(qry)
        body = cur.fetchall()
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(body)
    }



Original test conneciton code...


import json
import pymysql
import boto3

rds_host='terraform-20221012153942984900000003.cggdpmo6alkj.us-east-1.rds.amazonaws.com'
name='joseph'
password='ting1234'
db_name='mydb'


conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=20)


def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }






    \


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
name="joe"
empid=1235543

conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=20)

def lambda_handler(event, context):
    with conn.cursor() as cur:
        cur.execute("insert into Employee2 (EmpID, Name, input_day) values(%s, %s, %s)", (empid,name,today))
        cur.execute("select * from Employee2")







