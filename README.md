# weserve
## Description
WeServe is a call service agency that outsources customer service personnels 
to several companies.These agents are located in one call 
center. They receive calls from customers, and make calls to customers, in order to listen to complaints, and get feedback of products and services they have purchased from varying companies.These calls are recorded in the call log 
sheet, with some extra details saved in the call details sheet.The customer service managers would like to understand the activities of these call agents better. Hence, you have been provided with a sample of the sheets you need

## Tools
- Pandas
- boto3
- AWS redshift
- postgresql
- sqlalchemy
- AWS s3

## steps
- Extracted and cleaned the csv file using pandas
- loaded into the database (postgresql)
- built a data model, obtained my facts and dimensions
- built a s3 bucket(datalake) using boto3 and s3fs
- loaded into the datalake
- loaded from datalake to datawarehouse(redshift)