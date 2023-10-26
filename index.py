import pandas as pd
import psycopg2
import boto3
import redshift_connector as rdc
from sqlalchemy import create_engine
from configparser import ConfigParser

from cleaning.index import call_log, call_details
from utils.helper import create_bucket
from utils.helper import connect_to_dwh
from loading.create import raw_tables, transformed_table
from loading.transform import transformed_query

config = ConfigParser()
config.read('.env')

host = config['DB_CRED']['host']
user = config['DB_CRED']['username']
password = config['DB_CRED']['password']
database = config['DB_CRED']['database']

region = config['AWS']['region']
bucket_name = config['AWS']['bucket_name']
access_key = config['AWS']['access_key']
secret_key = config['AWS']['secret_key']

dwh_host = config['DWH']['host']
dwh_user = config['DWH']['username']
dwh_password = config['DWH']['password']
dwh_database = config['DWH']['database']
dwh_role = config['DWH']['role']


# estabilish your connection
conn = psycopg2.connect(
       host=host,
       user=user,
       password=password,
       database=database
)

cursor = conn.cursor()

# create bucket
# create_bucket(access_key, secret_key, bucket_name)

# extract from database to our datalake
db_conn = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:5432/{database}')

s3_path = 's3://{}/{}.csv'
db_tables = ['call_details', 'call_log']

for table in db_tables:
    
   query = f'SELECT * FROM {table}'
   df = pd.read_sql_query(query, db_conn)

   df.to_csv(
       s3_path.format(bucket_name, table)
       , index=False
       , storage_options={
           'key': access_key
           , 'secret': secret_key
       }
   )

# step 3: Create the raw schema in dwh
# connection to redshift
conn_details = {
  'host': dwh_host
   , 'user': dwh_user
   , 'password': dwh_password
   , 'database': dwh_database
} 

dwh_conn = connect_to_dwh(conn_details)
print('conn successful')


cursor = dwh_conn.cursor()

dev_schema = 'raw_data'
staging_schema = 'staging'

# cursor.execute(f'CREATE SCHEMA {dev_schema}')
# dwh_conn.commit()

# for query in raw_tables:
#     print(f'--------------{query[:20]}')
#     cursor.execute(query)
#     dwh_conn.commit()


# for table in db_tables:
#     query = f'''
#     copy {dev_schema}.{table} 
#     from '{s3_path.format(bucket_name, table)}'
#     iam_role '{dwh_role}'
#     delimiter ','
#     ignoreheader 1;
#     '''
#     cursor.execute(query)
#     dwh_conn.commit()
    

# step 4
cursor.execute(f'''CREATE SCHEMA {staging_schema}''')
dwh_conn.commit()

for query in transformed_table:
    cursor.execute(query)
    dwh_conn.commit()


for query in transformed_query:
    print(f'------------------------{query[:50]}')
    cursor.execute(query)
    dwh_conn.commit()


 # step 4
cursor.execute(f'''CREATE SCHEMA {staging_schema}''')
dwh_conn.commit()

for query in transformed_table:
    cursor.execute(query)
    dwh_conn.commit()


for query in transformed_query:
    print(f'------------------------{query[:20]}')
    cursor.execute(query)
    dwh_conn.commit()   