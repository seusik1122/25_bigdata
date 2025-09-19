your_book = [2002, '파이썬', 200]

print(your_book)
print(type(your_book))

year, title, size = your_book
print(year)
print(title)
print(size)

your_book[0] = 2005
print(your_book)

your_book.insert(1, '하이하이')
print(your_book)

your_book.remove('하이하이')
print(your_book)

new_book = your_book[0:2]
print(new_book)

new_book = your_book[:]
print(new_book)

your_book[0] = 2000
print(new_book)

list_value = ['1','2','3','4','5','6','7','8']
new_list_value = list_value[:]
list_value[0] = 11

print(new_list_value)
print(list_value)

list_value = [['1','2'],['3','4'],['5','6'],['7','8']]
list_value[0][0] = '11'
print(list_value)

tuple_list = tuple(list_value)
print(tuple_list)

list = list(tuple_list)
print(list)

for i in range(1,10):
    print(i)

for i in range(1, 10,2):
    print(i)