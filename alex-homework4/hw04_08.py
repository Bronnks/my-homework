chars = '!%@#$^&'


def check_password(password):
    if len(password) < 8:
        return print('Пароль не надежный')
    if password.isalnum() or any(i in chars for i in password):
        print('Пароль надежный')
        return

    print('Пароль не надежный')


x = input()
check_password(x)
