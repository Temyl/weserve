create table call_details(
	callID varchar primary key not null,
	callDurationInSeconds int,
	agentsGradeLevel varchar,
	callType varchar,
	callEndedByAgent bool
)

select * from call_details