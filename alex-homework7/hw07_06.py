def create_dict(lst):
    dct = {key:value for (key, value) in j.split() for j in lst}
    print(dct)


test = 'a 1, b 2, c 3'
create_dict(test)