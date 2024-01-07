chars = '!%@#$^&'


def check_password(password):
    count = 0
    if len(password) < 8 or ' ' in password:
        return print('Пароль не надежный')
    if password.isalnum or any(i in chars for i in password):
        count+=1
    if count < len(password):
        print('Пароль надежный')

    else:
        print('Пароль не надежный')


x = input()
check_password(x)
