
# -*- coding: utf-8 -*-
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

###############  连接数据文件 ########################
conn = sqlite3.connect('books.db')
c = conn.cursor()

select_cmd = " SELECT DISTINCT name FROM books ORDER BY name "
book_list = []

for row in c.execute(select_cmd):
    # print(row)
    book_list.append(*row)

print('《' + book_list[1] + '》')

book_name = book_list[1]
select_cmd = "SELECT chapter_content, chapter_name FROM books WHERE name = '" + book_name + "' ORDER BY  chapter_name"  #  "LIMIT 50"

# c.execute(select_cmd)
# r = c.fetchone()
# print(r[1])
# print(c.fetchall())

chapter_number = []
chapter_texts = []

c.execute(select_cmd)
r = c.fetchone()
while r != None :
    chapter_number.append( r[1])
    chapter_texts.append( r[0])
    # print(r[1])
    r = c.fetchone()

# print(chapter_number)
# print(chapter_texts[0])

c.close()

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

