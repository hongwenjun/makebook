# -*- coding: utf-8 -*-
import sqlite3 , re , copy

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

def chapter_style(s) :
    if s:
        try:
            if re.findall('^\d+\.', s)[0] :
                c = s.split('.')[1]
        except:
            c = s
    return c

###############         连接数据文件    ##############
conn = sqlite3.connect('books.db')
c = conn.cursor()

select_cmd = " SELECT DISTINCT name FROM books ORDER BY name "
book_list = []

for row in c.execute(select_cmd):
    book_list.append(*row)

###  按书名建立电子书
def make_book(book_name):
    chapter_number = []
    chapter_texts = []
    idx = []

    ###############     按书名读取章节记录   ##############
    select_cmd = "SELECT chapter_content, chapter_name FROM books WHERE name = '" + book_name + "' ORDER BY  chapter_name"

    c.execute(select_cmd)
    r = c.fetchone()
    while r != None :
        chapter_number.append( r[1])
        chapter_texts.append( r[0])
        r = c.fetchone()

    ###############     复制章节建立索引排序   ##############

    idx = copy.copy(chapter_number)
    strsort(idx)

    f_name = book_name + '.txt'
    f = open(f_name, 'w', encoding='utf-8')

    ###############     把数据输出到电子书文件   ##############

    f.write('《' + book_name + '》\n\n')
    text = []
    for id in range(len(idx)):
        print(idx[id])    # 章节索引 日志
        i = chapter_number.index(idx[id])
        title = chapter_style(chapter_number[i]) 
        f.write( title + '\n')
        
        text =  chapter_texts[i].replace(',\n,','\n')  
        text = text.replace( title , "")
        text="\n".join(text.split())
        f.write( text[1:-1] )
        f.write("\n\n")
    f.close()



### 所有电子书生成
for id in range(len(book_list)):
    print("《%s》:%d" %(book_list[id],id ))
    book_name = book_list[id]
    print('《' + book_name + '》')
    make_book(book_name)

c.close()