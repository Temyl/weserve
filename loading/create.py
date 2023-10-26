call_details = ''' CREATE TABLE IF NOT EXISTS Raw_data.call_details
(
    callid varchar primary key not null,
    calldurationinseconds integer,
    agentsgradelevel varchar,
    calltype varchar,
    callendedbyagent boolean
);
'''

call_log = ''' CREATE TABLE IF NOT EXISTS Raw_data.call_log
(
    id varchar primary key not null,
    callerid varchar,
    agentid integer,
    complainttopic varchar,
    assignedto double precision,
    status varchar,
    resolutiondurationinhours varchar
);
'''

ft_call_log = ''' CREATE TABLE IF NOT EXISTS staging.ft_call_log
(
    id BIGINT IDENTITY(1, 1),
    callid varchar,
    calldurationinseconds integer,
    agentsgradelevel varchar,
    assignedto double precision,
    agentid integer,
    callerid varchar,
    resolutiondurationinhours varchar
);
'''


dim_assigned_calls_resolved = ''' CREATE TABLE IF NOT EXISTS staging.dim_assigned_calls_resolved
(
    id BIGINT IDENTITY(1, 1),
    callerid varchar,
    assignedto double precision,
    status varchar
);
'''

dim_call_duration_and_grade_level = ''' CREATE TABLE IF NOT EXISTS staging.dim_call_duration_and_grade_level
(
     id BIGINT IDENTITY(1, 1),
     agentid integer,
     calldurationinseconds integer,
     agentsgradelevel varchar
)
'''
dim_agents_with_resolved_closed_case = ''' CREATE TABLE IF NOT EXISTS staging.dim_agents_with_resolved_imclosed_case
(
     id BIGINT IDENTITY(1, 1),
     agentid integer,
     status varchar,
     agentsgradelevel varchar
)
'''

dim_call_details = ''' CREATE TABLE IF NOT EXISTS staging.dim_call_details
(
     id BIGINT IDENTITY(1, 1),
     callerid varchar,
     complainttopic varchar,
     status varchar,
     calltype varchar,
     callendedbyagents boolean
)
'''

raw_tables = [call_log, call_details]
transformed_table = [ft_call_log, dim_agents_with_resolved_closed_case, dim_assigned_calls_resolved, dim_call_details, dim_call_duration_and_grade_level]
