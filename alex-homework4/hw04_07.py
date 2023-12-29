from random import choice
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def password(leng):
    res = ''
    for _ in range(leng):
        res += choice(chars)
    print(res)


x = int(input())
password(x)
