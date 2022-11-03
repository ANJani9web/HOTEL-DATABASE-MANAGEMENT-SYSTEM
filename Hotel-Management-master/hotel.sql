create database dine;
use dine;
CREATE TABLE dine_book(
  dineid int primary key,
  User_Id int(11) NOT NULL,
  Table_name varchar(20) NOT NULL,
  Guest tinyint(4) NOT NULL,
  Event_date date NOT NULL,
  Event_time time NOT NULL,
  Request varchar(30) NOT NULL,foreign key(User_Id) references register(User_Id)
);

select * from dine_book;
delete from dine_book where Event_date<=CURDATE();
drop table dine_book;
CREATE TABLE event_book (
  eventid int primary key,
  User_Id int(11) NOT NULL,
  Hall_name varchar(30) NOT NULL,
  Event_name text NOT NULL,
  Guest tinyint(4) NOT NULL,
  Event_date date NOT NULL,
  Start_time time NOT NULL,
  End_time time NOT NULL
);
select * from event_book;
drop table event_book;
CREATE TABLE `register` (
  `User_Id` int(11) NOT NULL primary key,
  `Name` varchar(50) NOT NULL,
  `Gender` varchar(6) NOT NULL,
  `Mob_no` bigint(12) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Password` varchar(12) NOT NULL,
  `Age` int(11) NOT NULL,
  `Country` varchar(5) NOT NULL,
  `State` varchar(20) NOT NULL,
  `City` varchar(20) NOT NULL,
  `Locality` varchar(20) NOT NULL,
  `Birth_date` text NOT NULL
);
select * from register;
drop table register;
CREATE TABLE `room_book` (
	`roomid` int primary key,
  `User_Id` int(11) NOT NULL,
  `Room_name` varchar(30) NOT NULL,
  `Arrival` date NOT NULL,
  `Departure` date NOT NULL,	
  `Rooms` tinyint(4) NOT NULL,
  `Adults` tinyint(4) NOT NULL,
  `Children` tinyint(4) NOT NULL
);
select * from event_book;
select * from dine_book;
select * from room_book;
drop table room_book;
insert into register values(2,"abc",'M',1111111111,"abc@gmail.com","12345678",20,"india","bohar","gya","gayanagar","01/01/2001");
select * from staff;
create table rooms(roomid int primary key,roomnumber int,User_Id int(11),foreign key (User_Id) references register(User_Id) on delete set null);
create table services(serviceid int primary key,id int,service varchar(200),roomid int,User_Id int(11),Password varchar(12),foreign key (id) references staff(id) on delete set null,foreign key (User_Id) references register(User_Id) on delete set null,foreign key (roomid) references room_book(roomid) on delete set null);
drop table services;
select * from services;
select * from register;
-- drop table room_book;
select * from room_book;



	

