“”“
MySQL
ENGINE(引擎)     DEFAULT CHARSET=utf8
“”“
create table class_1(    id int primary key auto_increment,
                        name varchar(30) not null,
                        age tinyint unsigned,
                        sex enum('m','w','o'),
                        score float default 0)
create table hobby(      id int primary key auto_increment,
                        name varchar(30) not null,
                        hobby set("sing","dance","draw"),
                        `level_zyp` char(2),
                        price decimal(7,2)
                        remark text)
show create table class_1;
drop table class_1;
insert into class_1 values
(1,"lilt",18,"w",92)

select * from class_1;

insert into class_1(name,age,sex,score)
values
("Abb",20，"m",100)
insert into class_1(name,age)
values
("lucy",18)
("luciiy",50)

insert into hobby(name,hobby,level_zyp,price,remark)
values
("dsg","sing","A",15800,"胡说八道")
("asd","sing,dance","b",66454.121,"净胡说")

select name,age,score from class_1;
select * from class_1 where id==1；
select * from class_1 where score between 70 and 80;(不能使用70<score<80)
select * from class_1 where score  not between 70 and 80;
select * from class_1 where age in (16,17,18);
select * from class_1 where age not in (16,17,18);
select * from class_1 where sex is null;(不能sex=null，值为空)
select * from class_1 where sex is not null;
select * from class_1 where sex ="m" and score>90;
select * from class_1 where not sex="m";
select * from class_1 where author in ("鲁迅","矛盾")#查找班级里面鲁迅或矛盾写的书
update class_1 set score=72 where name="lucy";
update class_1 set sex="m",score=91 where name="Alex";
update class_1 set score=score+1 where ;
delete from class_1 where name="joy";
select * from hobby;
alter table hobby
    add tel char(11) after price;
alter table hobby
    drop level_zyp;
alter table hobby
    modify tel char(16);
desc hobby;
alter table hobby
    change tel phone char(16);
desc hobby;
alter table class_1 rename cls;
show table;

create table marathon ( id int primary key auto_increment,
                        athlete varchar(32), birthday date,
                         r_time datetime comment "报名时间",
                          performance time );
insert into marathon values (1,"曹操","1998-2-16","2021/5/6 10:10:27","2:38:49"),
                            (2,"关羽","2000-7-19","2021/4/30 16:22:09","2:27:18"),
                            (3,"孙策","1995-10-23","2021/5/2 20:1:2","2:44:00");
select * from marathon where birthday >='1995-01-01';
select * from marathon where performance >='2:30:00';
select database();
select now():
select curtime();
select curdate():
alter table marathon modify registration_time datetime default now();
update book set price=45 where title="呐喊"；
alter table book
    add publication_time date after price;
update book set publication_time="2018-10-1"
    where author="老舍";
update book set publication_time="2020-10-1"
    where publication_time="中国文学出版社" and author !="老舍";
update book set publication_time="2022-10-1"
    where publication_time is null;
delete from book where price >65；
select * from cls where name like "L%";
select * from cls where name like "_____";
select * from cls where name regexp "^A.+";
select * from cls where name regexp "^.{3}$";
select * from class_1 as cls where name regexp "^.{3}$";(只针对这条语句有效)
select name as 姓名，age as 年龄 from class_1  where name regexp "^.{3}$";(只针对这条语句有效)
select * from cls order by score desc;
select * from cls order by score;
select * from cls where sex="m" order by score desc;
select * from cls where order by age desc,score desc;(年龄降序，分数降序)
select * from cls where sex="m" limit 2;
select name,score from cls where sex="m" order by score desc limit 1;
select name as 名字，score as 分数 from cls where sex="m" order by 分数 desc limit 1;
select * from cls where sex="m" union select * from cls where score>90;(不带重复)
select * from cls where sex="m" union all select * from cls where score>90;(带重复)
select name,age,score from cls where sex="m" union select name,age,score from cls where score>90;(字段必须一致)
select * from (select * from cls where sex="w") as w where score>90;(把子查询的结果作为where查询的对象)
select * from cls where score>(select name,score from cls where name="jbj") ;(子句结果作为一个值使用时，返回的结果需要一个明确值，不能是多行或者多列)
select * from cls where score in (select score from cls where name="abby" or name="Tom");
(如果子句结果作为一个集合使用，即where子句中是in操作，则结果可以是一个字段的多个记录.)
select name,age,score from cls where sex="m" order by score desc limit1;
select name,age,score from cls where sex="w" order by score desc limit1;

select max(attack) as 最大 from san_guo;
select count(name) as number from san_guo;(count不能统计空值)
select country, count(*) from san_guo group by country;
select country,from san_guo group by country,gender;
select * from san_guo where gender="男";
select country,count(id) from san_guo where gender="男" group by country;
select country,count(id) as number from san_guo where gender="男" group by country order by number desc;
select country,count(id) as number from san_guo where gender="男" group by country order by number desc limit 2;
select avg(price) from book group by author;
select distinct count ,gender from san_guo;(去重)
select count(distinct publication) from book;
select publication,avg(price) from book group by publication
having max(price)>50
order by avg(price) desc;
create index name_index on cls(name);
create unique index name_unique on cls(name);
show index from cls;
drop index score_unique on cls;
alter table person add constraint dept_fk foreign key(dept_id) references dept(id);
alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete cascade on update cascade;
alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete set null on update set null;

CREATE TABLE person (   id int PRIMARY KEY AUTO_INCREMENT,
                        name varchar(32) NOT NULL,
                        age tinyint unsigned,
                        salary decimal(10,2),
                        dept_id int ,
                        constraint dept_fk foreign key(dept_id) references dept(id) );
show create table person;
alter table person drop foreign key dept_fk;
drop index dept_fk on person;
“”“
朋友圈
“”“
-------用户表
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(64)
);
-------朋友圈表
create table pyq(
id int primary  key auto_increment,
image blob,
content text,
time datetime,
user_id int,
foreign key(user_id) references user(id)
);
----------点赞评论表,可以看做用户和朋友圈多对多关系
create table user_pyq(
id int primary key auto_increment,
'like' bit default 0,
content text default null
u_id int,
p_id int,
foreign key(u_id) references user(id),
foreign key(p_id) references pyq(id)
);
show create table pyq;
select * from cls,hobby where cls.name = hobby.name;(表名.字段名)
创建函数;
delimiter $$
create function stu() returns int
begin
return (select score from cls order by score desc limit 1);
end $$
delimiter ;
使用函数;
select stu();

create table 作家(
id int primary key auto_increment,
name varchar(30),
sex char,
remark text
);
create table 出版社(
id int primary key auto_increment,
pname varchar(30),
address char,
phone char(16)
);
create table 图书(
id int primary key auto_increment,
bname varchar(30),
price float,
a_id int,
P_id int,
foreign key (a_id) references 作家(id),
foreign key (p_id) references 出版社(id)
);

create table 作家_出版社(
id int primary key auto_increment,
签约时间 date,
aid int,
pid int,
foreign key (aid) references 作家(id),
foreign key (pid) references 出版社(id)
);
create function score(uid1 int,uid2 int)
return float
begin
declare s1 float;
declare s2 float;
select score from cls where id=uid1 into s1;
select score from cls where id=uid2 into s1;
return s1-s2;
end $$

