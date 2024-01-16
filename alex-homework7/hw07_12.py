def create_div_dict():
    res = {i: [j for j in range(1, i + 1) if i % j == 0] for i in range(1, 11)}
    print(res)


create_div_dict()
