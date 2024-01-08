chars = '!%@#$^&'


def check_password(password):
    if len(password) < 8 or ' ' in password:
        return print('Пароль не надежный')
    if password.isdigit() or password.isalpha() and password.isupper() or password.isalpha() and password.islower() or all(
            i in chars for i in password):
        print('Пароль не надежный')
    else:
        print('Пароль надежный')


x = input()
check_password(x)
