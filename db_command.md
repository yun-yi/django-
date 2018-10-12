### 一、ubuntu系统中Mysql5.7操作
1.启动数据库：sudo service mysql start

2.关闭数据库：sudo service mysql stop

3.重启数据库：sudo service mysql restart

4.查看数据库是否启动：ps -ef | grep mysql | grep grep

5.设置超级用户密码：sudo mysql_secure_installation

6.进入超级用户：sudo mysql -uroot -p密码

```angular2html
说明：
    进入普通账户同理，唯一需要注意的是需要指定IP：sudo mysql -uroot -p密码 -hIP
```

7.进入超级用户创建普通用户：CREATE USER '用户名'@'HOST' IDENTIFIED BY '密码';

```angular2html
说明：
    用户名：你将创建的用户名，
    HOST：指定该用户在哪个主机上可以登陆，如果是本地用户可用localhost，如果想让该用户可以从任意远程主机登陆，可以使用通配符%，
    密码：该用户的登陆密码，密码可以为空，如果为空则该用户可以不需要密码登陆服务器
```
8.给普通用户权限：GRANT privileges ON dbname.tbname TO '用户名'@'HOST'

```angular2html
说明:
    privileges：用户的操作权限，如SELECT，INSERT，UPDATE等，如果要授予所的权限则使用ALL
    dbname：数据库名
    tbname：表名，如果要授予该用户对所有数据库和表的相应操作权限则可用*表示，如*.*
```

9.设置与更改用户密码：SET PASSWORD FOR '用户名'@'HOST' = PASSWORD('新密码');

10.如果是当前登陆用户用:SET PASSWORD = PASSWORD("新密码")

11.撤销用户权限：REVOKE privilege ON dbname.tbname FROM '用户名'@'HOST';

```angular2html
说明:
    privilege, dbname, tbname：同授权部分
```

12.删除用户:DROP USER '用户名'@'HOST';

13.创建数据库:create database 库名 default charset utf8;

14.创建表:create table 表名(
写字段
)

15.复制表:create table 新表名 select * from 表名(后面可以跟条件);

16.插入数据:


### 二、ubuntu系统中MongoDB操作

1.启动数据库:service mongod start

2.进入数据库:mongo

3.切换到指定数据库:use 数据库名

4.查看数据库所有数据:db.数据库名.find()

5.查看所有数据库:show dbs

6.查看当前数据库的连接机器地址:db.getMongo()

7.创建一个聚集集合(table):db.createCollection(“collName”, {size: 20, capped: 5, max: 100});

8.得到指定名称的聚集集合(table):db.getCollection("account");

9.得到当前db的所有聚集集合:db.getCollectionNames();

10.显示当前db所有聚集索引的状态:db.printCollectionStats();

11.添加一个用户:db.addUser("name");

    db.addUser("userName", "pwd123", true); 添加用户、设置密码、是否只读

12.数据库认证、安全模式:db.auth("userName", "123123");

13.显示当前所有用户:show users;

14.删除用户:db.removeUser("userName");

### 三、ubuntu系统中Redis操作

1.查看数据库是否启动:ps aux | grep redis | grep grep

2.启动数据库:

```angular2html
    指定路径操作:sudo /etc/init.d/redis-server start
    用服务操作:service redis-server start
```

3.重启数据库:

```angular2html
    指定路径操作:sudo /etc/init.d/redis-server restart
    用服务操作:service redis-server restart
```

4.关闭数据库:

```angular2html
    指定路径操作:sudo /etc/init.d/redis-server stop
    用服务操作:service redis-server stop
```

5.连接客户端:redis-cli -h HOST -p 6379 -a 密码 -->默认是没有密码的，需要更改配置文件

6.配置文件：

```angular2html
    1)找到配置文件: whereis redis.conf
    2)打开配置文件: vim /etc/redis/reids.conf --> 这是我电脑的路径
    3)在命令模式下输入: /requirepass password
    4)在编辑模式下将password改成你自己想设置的密码
    5)在命令模式下输入: :wq   -->保存退出
    6)重启redis即可生效: 见步骤3.重启数据库
```

7.如果要允许远程连接，需要配置文件：
 
```angular2html
    1)找到配置文件: whereis redis.conf
    2)打开配置文件: vim /etc/redis/reids.conf --> 这是我电脑的路径
    3)在命令模式下输入： /bind 127.0.0.1 ::1
    4)在编辑模式下将bind 127.0.0.1 ::1 改成bind 0.0.0.0 ::1
    5)在命令模式下输入: :wq  -->保存退出
    6)重启redis即可生效: 见步骤3.重启数据库
```

### Ubuntu系统下使用Postpresql

1.创建数据库:create database 数据库名;

2.查看数据库:\l

3.删除数据库:drop database 数据库名;--->返回 drop database

4.创建表:

```angular2html
    create table 表名(
        char(),-->固定长度字符串
        character(),-->固定长度字符串
        varchar(),-->可变字符串长度
        integer(),-->储存整数
        primary key ()-->设置主键
    );
```

5.查询表:\d

6.查询表结构:\d 表名

7.删除表:drop table 表名;--->返回 drop table

8.插入数据:insert into 表名(字段1,字段2..) values (字段1对应数据, 字段2对应数据...);

9.查询数据:select 查询字段 from 表名;

10.跟新数据:update 表名 set 字段1=数据1, 字段2=数据2... where 条件;
    
11.删除数据:delete from 表名 where 条件;

12.排序:

```angular2html
    SELECT column-list 
    FROM table_name 
    [WHERE condition] 
    [ORDER BY column1, column2, .. columnN] [ASC | DESC];
```

>参数说明:

    column_list：它指定要检索的列或计算。
    table_name：它指定要从中检索记录的表。
    FROM子句中必须至少有一个表。
    WHERE conditions：可选。它规定必须满足条件才能检索记录。
    ASC：也是可选的。它通过表达式按升序排序结果集(默认，如果没有修饰符是提供者)。
    DESC：也是可选的。 它通过表达式按顺序对结果集进行排序。
    
13.分组:

```angular2html
    SELECT column-list  
    FROM table_name  
    WHERE [conditions ]  
    GROUP BY column1, column2....columnN  
    ORDER BY column1, column2....columnN
```

>注意：在GROUP BY多个列的情况下，您使用的任何列进行分组时，要确保这些列应在列表中可用。

14.子查询:

```angular2html
    SELECT column1, column2  
    FROM table1, table2  
    WHERE [ conditions ]  
    GROUP BY column1, column2  
    HAVING [ conditions ]  
    ORDER BY column1, column2
```

>举例:显示名称(name)数量小于2的记录
    
    SELECT NAME   
    FROM EMPLOYEES  
    GROUP BY NAME HAVING COUNT (NAME) < 2;

15.条件查询,它们通常与WHERE子句一起使用: and, or, not, like, in, not in, between

16.内连接:内部连接也被称为连接或简单连接(类似求交集)

```angular2html
   SELECT table1.columns, table2.columns  
    FROM table1  
    INNER JOIN table2  
    ON table1.common_filed = table2.common_field; 
```

17.左外连接:左外连接返回从“ON”条件中指定的左侧表中的所有行，只返回满足条件的另一个表中的行。

```angular2html
    SELECT table1.columns, table2.columns  
    FROM table1  
    LEFT OUTER JOIN table2  
    ON table1.common_filed = table2.common_field;
```

18.右外连接:右外连接返回从“ON”条件中指定的右侧表中的所有行，只返回满足条件的另一个表中的行。

```angular2html
    SELECT table1.columns, table2.columns  
    FROM table1  
    RIGHT OUTER JOIN table2  
    ON table1.common_filed = table2.common_field;

```

19.全外连接:全外连接从左表和左表中返回所有行。 它将不满足条件的返回为NULL。

```angular2html
    SELECT table1.columns, table2.columns  
    FROM table1  
    FULL OUTER JOIN table2  
    ON table1.common_filed = table2.common_field;
```

20.交叉连接:跨连接(CROSS JOIN)将第一个表的每一行与第二个表的每一行相匹配。 它也被称为笛卡尔积。 如果table1具有“x”行，而table2具有“y”行，则所得到的表将具有(x * y)行。

```angular2html
    SELECT coloums   
    FROM table1   
    CROSS JOIN table2
```