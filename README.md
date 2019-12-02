# makebook
自己整理电子书，Python Sqlite 学习代码笔记历史


### Scrapy 官方中文文档
- Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 可以应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中。
- https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/overview.html

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


### 使用正则能够排序“数字文本”，能够按标题排序
```python
import sqlite3 , re

def sort_key(s):
    # 排序关键字匹配
    # 匹配开头数字序号
    if s:
        try:
            c = re.findall('^\d+', s)[0]
        except:
            c = -1
        return int(c)

def strsort(alist):
    alist.sort(key=sort_key)
    return alist

#### 复制章节建立索引排序  ###

idx = chapter_number
strsort(idx)

f_name = book_list[1] + '.txt'
f = open(f_name, 'w', encoding='utf-8')

for id in range(len(idx)):
    print(idx[id])    # 章节索引 日志
    i = chapter_number.index(idx[id])
    f.write( chapter_number[i] )
    f.write( chapter_texts[i].replace(',\n,','\n') )
    f.write("\n")

f.close()

```

### 使用join和split，删除'\xA0'分割和删除逗号分割
```python

f_name = book_name + '.txt'
f = open(f_name, 'w', encoding='utf-8')

###############     把数据输出到电子书文件   ##############
f.write('《' + book_name + '》\n\n')
text = []
for id in range(len(idx)):
    print(idx[id])    # 章节索引 日志
    i = chapter_number.index(idx[id])
    f.write( chapter_number[i] )
    text =  chapter_texts[i].replace(',\n,','\n')  
    text="\n".join(text.split())
    f.write( text[1:-1] )
    f.write("\n")

# print( text[1:-1] )

f.close()
```

### 测试结果
```
python.exe  make_book.py

《一不小心就无敌啦》:0  《万古神帝》:1  《万道剑尊》:2  《九天神皇》:3  《亲吻我的无良校草》:4  《亿万盛宠只为你》:5    《从我是特种兵开始打卡》:6      《从火凤凰开始的特种兵》:7      《仙医帝妃》:8  《余生有你，甜又暖》:9
《余生皆是喜欢你》:10   《修真聊天群》:11       《倾城小美人：寒王宠上瘾》:12   《全职法师》:13 《农家小福女》:14       《冷傲女王玩转校园》:15 《凌天战尊》:16 《凤鸾九霄》:17 《别闹，薄先生！》:18   《医妃惊世》:19 《召唤之
绝世帝王》:20   《吃定小白兔：狐狸总裁别惹我》:21       《喜劫良缘，纨绔俏医妃》:22     《墨少蚀骨宠：甜妻，请入怀》:23 《天唐锦绣》:24 《天才修炼师：至尊狂凤》:25     《女配表示很无辜》:26   《官场美人》:27 《官神》:28
《帝少的专属：小甜心，太缠人》:29       《弃妃，你又被翻牌了！》:30     《恶魔老公不外卖》:31   《惊世第一杀手妃：邪王狂妻》:32 《慕爱成婚，高冷上司住隔壁》:33 《我的绝色美女房客》:34 《新妻上岗，总裁，狠狠爱！》:35 《无敌医
神都市纵横》:36 《校花的贴身高手》:37   《武神血脉》:38 《殿下专属小丫头》:39   《混在三国争天下》:40   《混在大唐的工科宅男》:41       《烂柯棋缘》:42 《爆萌小仙：扑倒冰山冷上神》:43 《爱妃，宠你上了瘾》:44 《特工王妃：冷傲
王爷腹黑妻》:45 《狂妃狠绝色：邪王圈宠下堂妃》:46       《生活系男神》:47       《皇室老公专宠迷糊小心肝》:48   《神医凰后》:49 《神医小萌妃：帝尊，太难撩！》:50       《神医弃女》:51 《神医狂妃，废材三小姐》:52     《纵意人
生》:53 《至尊特工》:54 《萌妻甜甜圈：亿万暖婚第7天》:55        《萌宠甜心：恶魔少爷深深吻》:56 《蜜恋百分百：恶魔少爷，宠翻天！》:57   《谍影风云》:58 《豪门错爱I，总裁太危险》:59    《邪王追妻》:60 《都市之无限选择系统》:61
《都市极品医神》:62     《都市绝品仙医》:63     《都市绝武医神》:64     《都市超级医圣》:65 《重生军工子弟》:66 《重生大唐当奶爸》:67   《重生逍遥君王》:68     《霸总离开我就活不了》:69       《驭房有术》:70 《魅医倾城》:71


time py all_book.py > ok.txt

books.db   890M 导出 72本书
机械硬盘 235秒， 固态硬盘 131秒

Process returned 0 (0x0)   execution time : 131.585 s
进程返回 0 (0x0)   执行时间 : 131.585 秒
```