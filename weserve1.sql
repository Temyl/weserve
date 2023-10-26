select * from call_details
--total number of calls received vs resolved
select callerid, status from call_log
where status = 'resolved';

--total number of calls resolved vs calls asigned
select callerid, assignedto, status
from call_log 
where status = 'resolved'

update call_details
set callid = '1'
where callid = 'ageentsGradeLevel';

select * from call_log
 -- changing data type of id in call_log
alter table call_log
alter id set data type varchar 

--  make id in call_log to foreign key 
alter table call_log
add constraint fk_callid
foreign key (id)
references call_details(callid);

--call durstion and grade level of the agents
select agentid, calldurationinseconds, agentsgradelevel
from call_details cd
left join call_log cl
on cd.callid = cl.id

--closed and resolved cases, the grade level of the agents
select id, agentid, status, agentsgradelevel
from call_details cd
left join call_log cl
on cd.callid = cl.id
where status = 'resolved' 
OR status = 'CLOSED';
