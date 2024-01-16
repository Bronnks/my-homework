def create_pal_list():
    res = [i for i in range(1, 101) if str(i)[0] == str(i)[-1]]
    print(res)


create_pal_list()
