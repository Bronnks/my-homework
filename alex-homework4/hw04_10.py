chars = '!%@#$^&'


def check_password(password):
    count = 0
    if len(password) < 8:
        return print('Пароль не надежный')
    for i in password:
        if i in chars or i.isalnum():
            count += 1
    if count < len(password):
        print('Пароль надежный')

    else:
        print('Пароль не надежный')


x = input()
check_password(x)
