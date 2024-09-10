MYSQL SCRIPTS

USE dbtest;

CREATE TABLE EMPLOYEES (
ID int,
F_NAME varchar(255),
L_NAME VARCHAR(255));

insert into EMPLOYEES values (1, "DAMITH","BANDARA");
insert into EMPLOYEES values (1, "SUNIL","PERERA");
COMMIT;


POSTGRES SCRIPTS

create table Employees (id int,
f_name varchar(255),
l_name varchar(255));