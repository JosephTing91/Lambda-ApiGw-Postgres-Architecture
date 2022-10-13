#this program is for creating a table in mysql and 
import json
import pymysql
import boto3
import logging
import sys
import base64
from datetime import date

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ssm=boto3.client('ssm', 'us-east-1')

password2 = ssm.get_parameter(
    Name='db_password',
    WithDecryption=False
)['Parameter']['Value']



secret_name = "dbcredentials"
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
    print(secret)

db_name='mydb'
today=date.today()


name='joseph'
password="ting1234"
rds_host="terraform-20221012234135840300000005.cggdpmo6alkj.us-east-1.rds.amazonaws.com"
conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=20)

def lambda_handler(event, context):

    name="joe"
    userid=189380987
    today=date.today()
    
    with conn.cursor() as cur:

        cur.execute('insert into Apptable (UserID, Name, input_date) values(%s, %s, %s)', (userid, name, today))
        conn.commit()
        cur.execute("select * from Apptable")
        for row in cur:
            logger.info(row)
            print(row)
    conn.commit()
conn.commit()






secret_name = "dbcredentials"
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
    host2=secret['host']
    username2=secret['username']
    password2=secret['password']
    print(host2)
    print(username2)
    print(password2)
db_name='mydb'
today=date.today()


name='joseph'
password="ting1234"
rds_host="terraform-20221012234135840300000005.cggdpmo6alkj.us-east-1.rds.amazonaws.com"
conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=20)

def lambda_handler(event, context):

    name="joe"
    userid=1891091287
    today=date.today()
    
    with conn.cursor() as cur:

        cur.execute('insert into Apptable (UserID, Name, input_date) values(%s, %s, %s)', (userid, name, today))
        conn.commit()
        cur.execute("select * from Apptable")
        for row in cur:
            logger.info(row)
            print(row)
    conn.commit()
conn.commit()






#first run function from here below with create table included... then change.... 



#this program is for creating a table in mysql and 
import json
import pymysql
import boto3
import logging
import sys
import base64
from datetime import date

logger = logging.getLogger()
logger.setLevel(logging.INFO)

secret_name = "dbcredentials"
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
  #  decryptedkeys=json.loads(secret)  # returns the secret as dictionary
  #  print(decryptedkeys)

db_name='mydb'
today=date.today()


name='joseph'
password="ting1234"
rds_host="terraform-20221012234135840300000005.cggdpmo6alkj.us-east-1.rds.amazonaws.com"
conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=20)

def lambda_handler(event, context):

    name="joe"
    userid=3214124323838337
    today=date.today()
    
    with conn.cursor() as cur:

        cur.execute('insert into Apptable (UserID, Name, input_date) values(%s, %s, %s)', (userid, name, today))
        conn.commit()
        cur.execute("select * from Apptable")
        for row in cur:
            logger.info(row)
            print(row)
    conn.commit()
conn.commit()

#        cur.execute("create table Apptable ( UserID  int NOT NULL, Name varchar(255) NOT NULL, input_date DATE, PRIMARY KEY (UserID))")
#        cur.execute("create table Apptable ( UserID  int NOT NULL, Name varchar(255) NOT NULL, input_date DATE, PRIMARY KEY (UserID))")