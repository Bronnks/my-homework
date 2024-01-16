from math import factorial as f
def create_fact_dict():
    res = {i:f(i) for i in range(1,11)}
    print(res)

create_fact_dict()