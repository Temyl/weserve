dim_assigned_calls_resolve = ''' INSERT INTO staging.dim_assigned_calls_resolve
(
    callerid,
    assignedto,
    status AS status(resolved)
) 
select callerid, assignedto, status
from call_log 
where status = 'resolved';

'''

dim_call_duration_and_grade_level = ''' INSERT INTO staging.dim_call_duration_and_grade_level
(
     agentid,
     calldurationinseconds,
     agentsgradelevel
)
select agentid, calldurationinseconds, agentsgradelevel
from call_details cd
left join call_log cl
on cd.callid = cl.id
'''

dim_agents_with_resolved_closed_case = ''' INSERT INTO staging.dim_agents_with_resolved_closed_case
(
     agentid,
     status,
     agentsgradelevel
)
select id, agentid, status, agentsgradelevel
from call_details cd
left join call_log cl
on cd.callid = cl.id
where status = 'resolved' 
OR status = 'CLOSED';
'''

dim_call_details = ''' INSERT INTO staging.dim_call_details
(
     callerid,
     complainttopic,
     status,
     calltype,
     callendedbyagents
)
select callerid, complainttopic, status, calltype, callendedbyagents
from call_details cd
left join call_log
on cd.callid = cl.id
'''
ft_call_log = ''' INSERT INTO staging.ft_call_log
(
    callid ,
    calldurationinseconds,
    agentsgradelevel,
    assignedto,
    agentid,
    callerid,
    resolutiondurationinhours
);
select callid, calldurationinseconds, agentsgradelevel, assignedto, agentid, callerid, resolutiondurationinhours 
from call_log cl
left join call_details cd
on cl.id = cd.callid
'''

transformed_query = [ft_call_log, dim_agents_with_resolved_closed_case, dim_assigned_calls_resolve, dim_call_details, dim_call_duration_and_grade_level]
