x = list(map(int, input().lstrip('[').rstrip(']').split(', ')))
match x:
    case []:
        print(0)
    case _:
        print(sum(i for i in x if i % 2 == 0))
