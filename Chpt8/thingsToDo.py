#Thing 1
print('---Thing 1---')
test1 = 'This is a test of the emergency text system'
test1Out =  open('test.txt', 'wt')
test1Out.write(test1)
test1Out.close()

#Thing 2
print('---Thing 2---')
test2In = open('test.txt', 'rt')
test2 = test2In.read()
test2In.close()
print (test2)
print("Does test1 = test2:", (test1 == test2))

#Thing 3
print('---Thing 3---')
booksCSVOut = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"'''
test3Out = open('books.csv', 'wt')
test3Out.write(booksCSVOut)
test3Out.close()

#Thing 4
print('---Thing 4---')
import csv
with open('books.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]
print(books)

#Thing 5
print("---Thing 5---")
books2CSVOut = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Steet Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''
test5Out = open('books2.csv', 'wt')
test5Out.write(books2CSVOut)
test5Out.close()

#Thing 6
print("---Thing 6---")
import sqlite3
conn = sqlite3.connect(':memory:')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
(title TEXT primary key,
author TEXT,
year INT)''')

#Thing 7
print('---Thing 7---')
with open('books2.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    books2 = [row for row in cin]
print(books2)
ins = 'INSERT INTO books (title, author, year) VALUES(?, ?, ?)'
for key in books2:
    curs.execute(ins, (key['title'], key['author'], key['year']))
    
#Thing 8
print('---Thing 8---')
curs.execute('SELECT title FROM books ORDER BY title')
thing8Result = curs.fetchall()
for title in thing8Result:
    print(title[0])

#Thing 9
print('---Thing 9---')
curs.execute('SELECT * FROM books ORDER BY year')
thing9Result = curs.fetchall()
for row in thing9Result:
    print("{} {} {}".format(row[0], row[1], row[2]))

curs.close()

#Thing 10
print('---Thing 10---')
import sqlalchemy as sa
saConn = sa.create_engine('sqlite://')
thing10Rows = conn.execute('SELECT title FROM books ORDER BY title')
for thing10Row in thing10Rows:
    print(thing10Row[0])

conn.close()

#Thing 11
print('---Thing 11---')
import redis
thing11Conn = redis.Redis()
thing11Conn.set("count", 1)
thing11Conn.set('name', 'Fester Bestertester')
print(thing11Conn.keys('*'))
print(thing11Conn.mget(['count', 'name']))

#Thing 12
print('---Thing 12---')
thing11Conn.incr('count')
print(thing11Conn.get('count'))
