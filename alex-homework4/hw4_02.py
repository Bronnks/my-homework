lst = ["apple", "banana", "cherry"]
res = map(lambda x: x[::-1], lst)

print(*res, sep='\n')
