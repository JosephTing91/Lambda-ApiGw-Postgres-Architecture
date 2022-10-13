
#this program is for creating a table in mysql and 
import json
import pymysql
import boto3
import logging
import sys
from datetime import date

logger = logging.getLogger()
logger.setLevel(logging.INFO)

secret_name = "dbsecrets2"
region_name = "us-east-1"

# Create a Secrets Manager client
client = boto3.client(
    service_name='secretsmanager',
    region_name=region_name
)

# In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
# See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
# We rethrow the exception by default.

get_secret_value_response = client.get_secret_value(
    SecretId=secret_name)


if 'SecretString' in get_secret_value_response:
    secret = get_secret_value_response['SecretString']
    # print(secret)
    decryptedkeys=json.loads(secret)  # returns the secret as dictionary  
    name=decryptedkeys['username']
    password=decryptedkeys['password']
    rds_host=decryptedkeys['host']

db_name='mydb'
today=date.today()
conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=20)

def lambda_handler(event, context):

    name="joe"
    userid=113244122234534321589987
    today=date.today()
    
    with conn.cursor() as cur:

        cur.execute("create table Apptable5 ( UserID  int NOT NULL, Name varchar(255) NOT NULL, input_date DATE, PRIMARY KEY (UserID))")
        cur.execute('insert into Apptable5 (UserID, Name, input_date) values(%s, %s, %s)', (userid, name, today))
        conn.commit()
        cur.execute("select * from Apptable5")
        for row in cur:
            logger.info(row)
            print(row)
    conn.commit()

#        cur.execute("create table Apptable ( UserID  int NOT NULL, Name varchar(255) NOT NULL, input_date DATE, PRIMARY KEY (UserID))")