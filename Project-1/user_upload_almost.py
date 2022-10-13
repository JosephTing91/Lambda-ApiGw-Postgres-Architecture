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



def decrypt(session, secret):
    client = session.client('kms')
    plaintext = client.decrypt(
        CiphertextBlob=bytes(base64.b64decode(secret))
    )
    return plaintext["Plaintext"]

session=boto3

print(decrypt(session, password2))


name2=ssm.get_parameter(
    Name='db_username',
    WithDecryption=True
)['Parameter']['Value']

rds_hostbad=ssm.get_parameter(
    Name='db_endpoint',
    WithDecryption=True
)['Parameter']['Value']


print(rds_hostbad)
print(name2)
print(password2)


db_name='mydb'
today=date.today()


name='joseph'
password="ting1234"
rds_host="terraform-20221012234135840300000005.cggdpmo6alkj.us-east-1.rds.amazonaws.com"
conn=pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=20)

def lambda_handler(event, context):

    name="joe"
    userid=189321380987
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