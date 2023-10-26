import pandas as pd


# read call_log file
call_log = pd.read_csv('C:/Users/DUNSIN/Downloads/Final Project/Final Project/call_log.csv')

# replacing the empty rows in the assignedto column with the agentID
call_log['assignedTo'] = call_log['assignedTo'].fillna(call_log['agentID'])

# replacing the empty rows in resolutiondurationhours to 'pending' and changing the datatype
call_log['resolutionDurationInHours'] = call_log['resolutionDurationInHours'].astype(object)
call_log['resolutionDurationInHours'] = call_log['resolutionDurationInHours'].fillna('pending')

call_log = pd.DataFrame(call_log)
call_log.to_csv('cleaned_call_log.csv', index=False)

# read call_details file
call_details = pd.read_csv('C:/Users/DUNSIN/Downloads/Final Project/Final Project/call_details.csv')

# replace the row with Inbound to in-bound in the callType column
call_details['callType'] = call_details['callType'].replace('Inbound', 'in-bound')

call_details = pd.DataFrame(call_details)
call_details.to_csv('cleaned_call_details.csv', index=False)


call_details.info()
call_log.info()
