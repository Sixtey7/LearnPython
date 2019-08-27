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
