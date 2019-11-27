# makebook
自己整理电子书，Python Sqlite 学习代码笔记历史

---
### :heart_eyes:  SQLite导入CSV数据.txt
<details>
<summary>点击展开内容</summary>

```
SQLite version 3.26.0 2018-12-01 12:34:55
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.

#  .mode MODE ?TABLE?       	设定输出模式
#  .import FILE TABLE       	将数据从FILE导入TABLE
#  .schema ?PATTERN?        	显示与PATTERN匹配的CREATE语句
#  .save FILE               	将内存数据库写入FILE

sqlite> .mode csv
sqlite> .import test.csv books

sqlite> .schema books
CREATE TABLE books(
  "_type" TEXT,
  "chapter_content" TEXT,
  "chapter_name" TEXT,
  "name" TEXT
);

sqlite> SELECT name FROM books LIMIT 5 ;

sqlite> .save books.db

#############################################################################

sqlite> .help
.archive ...             	管理SQL档案
.auth ON|OFF             	显示授权者回调
.backup ?DB? FILE        	备份数据库（默认为“ main”）到FILE
.bail on|off             	遇到错误后停止。默认关闭
.binary on|off           	打开或关闭二进制输出。默认关闭
.cd DIRECTORY            	将工作目录更改为DIRECTORY
.changes on|off          	显示由SQL更改的行数
.check GLOB              	如果由于.testcase不匹配而输出失败
.clone NEWDB             	从现有数据库将数据克隆到NEWDB
.databases               	列出附加数据库的名称和文件
.dbconfig ?op? ?val?     	列出或更改sqlite3_db_config（）选项
.dbinfo ?DB?             	显示有关数据库的状态信息
.dump ?TABLE? ...        	将所有数据库内容呈现为SQL
.echo on|off             	打开或关闭命令回显
.eqp on|off|full         	启用或禁用自动的EXPLAIN QUERY PLAN
.excel                   	在电子表格中显示下一个命令的输出
.exit ?CODE?             	使用返回码CODE退出此程序
.expert                  	实验性的。建议指定查询的索引
.fullschema ?--indent?   	显示模式和sqlite_stat表的内容
.headers on|off          	打开或关闭标题显示
.help ?-all? ?PATTERN?   	显示PATTERN的帮助文本
.import FILE TABLE       	将数据从FILE导入TABLE
.imposter INDEX TABLE    	在索引INDEX上创建冒名顶替者表TABLE
.indexes ?TABLE?         	显示索引名称
.limit ?LIMIT? ?VAL?     	显示或更改SQLITE_LIMIT的值
.lint OPTIONS            	报告潜在的架构问题。
.load FILE ?ENTRY?       	加载扩展库
.log FILE|off            	打开或关闭登录。 FILE可以是stderr / stdout
.mode MODE ?TABLE?       	设定输出模式
.nullvalue STRING        	使用STRING代替NULL值
.once (-e|-x|FILE)       	仅将下一个SQL命令的输出输出到FILE
.open ?OPTIONS? ?FILE?   	关闭现有数据库并重新打开FILE
.output ?FILE?           	将输出发送到FILE或stdout（如果省略FILE）
.print STRING...         	打印文字STRING
.prompt MAIN CONTINUE    	替换标准提示
.quit                    	退出程序
.read FILE               	从FILE读取输入
.restore ?DB? FILE       	从FILE恢复DB的内容（默认为“ main”）
.save FILE               	将内存数据库写入FILE
.scanstats on|off        	打开或关闭sqlite3_stmt_scanstatus（）指标
.schema ?PATTERN?        	显示与PATTERN匹配的CREATE语句
.selftest ?OPTIONS?      	运行SELFTEST表中定义的测试
.separator COL ?ROW?     	更改列和行分隔符
.sha3sum ...             	计算数据库内容的SHA3哈希
.shell CMD ARGS...       	在系统外壳中运行CMD ARGS ...
.show                    	显示各种设置的当前值
.stats ?on|off?          	显示统计信息或打开或关闭统计信息
.system CMD ARGS...      	在系统外壳中运行CMD ARGS ...
.tables ?TABLE?          	列出与LIKE模式TABLE匹配的表的名称
.testcase NAME           	开始将输出重定向到“ testcase-out.txt”
.timeout MS              	尝试打开锁定的表，以毫秒为单位
.timer on|off            	打开或关闭SQL计时器
.trace FILE|off          	在运行时输出每个SQL语句
.vfsinfo ?AUX?           	有关顶级VFS的信息
.vfslist                 	列出所有可用的VFS
.vfsname ?AUX?           	打印VFS堆栈的名称
.width NUM1 NUM2 ...     	设置“列”模式的列宽



============================================

SELECT * FROM books WHERE name = '九天神皇' 
   		ORDER BY  chapter_content  LIMIT 200


#####################################   
SQL 基础教程
https://www.w3school.com.cn/sql/index.asp

SQL SELECT DISTINCT 语句
在表中，可能会包含重复值。这并不成问题，不过，有时您也许希望仅仅列出不同（distinct）的值。

关键词 DISTINCT 用于返回唯一不同的值。

## 获得书名   SELECT DISTINCT 列名称 FROM 表名称

SELECT DISTINCT name FROM books ORDER BY name

```

</details>