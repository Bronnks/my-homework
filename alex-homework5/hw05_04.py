book = input().split(', ')
print(f'{book[1].split()[1]}, {book[1].split()[0]}. {book[0]}. {book[2]}.')
print('%s, %s. %s. %s.' % (book[1].split()[1], book[1].split()[0], book[0], book[2]))
print('{}, {}. {}. {}.'.format(book[1].split()[1], book[1].split()[0], book[0], book[2]))
