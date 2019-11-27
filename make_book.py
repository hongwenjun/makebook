
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('books.db')
c = conn.cursor()

select_cmd = " SELECT DISTINCT name FROM books ORDER BY name "
book_list = []

for row in c.execute(select_cmd):
    # print(row)
    book_list.append(*row)

print('《' + book_list[1] + '》')

book_name = book_list[1]
select_cmd = "SELECT chapter_content, chapter_name FROM books WHERE name = '" + book_name + "' ORDER BY  chapter_name  LIMIT 5"

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

f_name = book_list[1] + '.txt'
f = open(f_name, 'w', encoding='utf-8')
for i in range(len(chapter_number)):
    print(chapter_number[i])
    f.write( chapter_number[i] )
    f.write( chapter_texts[i] )
    f.write("\n")
    
f.close()

