# The main script that executes all the steps:

import os

# from dotenv import load_dotenv
# load_dotenv()

from src.extract import extract_transactional_data
from src.transform import remove_duplicates
from src.load_data_to_s3 import df_to_s3

# import variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")

# make a connection to redshift and extract transactional data with transformation tasks
print("Extracting and transforming data from the warehouse")
online_trans_cleaned = extract_transactional_data(dbname, host, port, user, password)

online_trans_cleaned = remove_duplicates(online_trans_cleaned)
print("the size of data after removing duplicates", online_trans_cleaned.shape)

# load the data to s3
key = 'etl_pipeline/docker/cm_online_transactions_v2.pkl'
s3_bucket = 'july-bootcamp'
df_to_s3(online_trans_cleaned, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)
