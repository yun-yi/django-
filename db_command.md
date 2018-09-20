#### 一、ubuntu系统中Mysql5.7操作
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


#### 二、ubuntu系统中MongoDB操作

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