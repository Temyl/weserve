import pandas as pd
from pandas import StringDtype

# extracting the file

call_details = pd.read_csv('C:/Users/DUNSIN/Downloads/Final Project/Final Project/call_details.csv')

call_log = pd.read_csv('C:/Users/DUNSIN/Downloads/Final Project/Final Project/call_log.csv')

# checking the table
# call_details.info()
# call_log.info()
# print(call_log.head(30))

# filling the missing assigned to columuns with agentID
call_log['assignedTo'].fillna(call_log['agentID'], inplace=True)

# filling the empty resolution duration column with 'not closed'
call_log['resolutionDurationInHours'].fillna('still resolving complaint', inplace=True)

# change datatype
call_log['assignedTo'] = call_log['assignedTo'].astype(int)
call_log['resolutionDurationInHours'] = call_log['resolutionDurationInHours'].astype(str)


# save the cleaned call_log to csv
call_log.to_csv('call_log.csv', index=True)

# changing the inbound to in-bound in the call_details table
call_details['callType'] = call_details['callType'].replace('Inbound', 'in-bound')

# save the cleaned call_details to csv
call_details.to_csv('call_details.csv', index=True)
call_log.info()






