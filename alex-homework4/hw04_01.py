list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = ["%", "$", "@"]
res = list(zip(list1, list2, list3))
print(*res, sep='\n')

