chars = '!%@#$^&'
def check_password(password):
    if len(password) < 8:
        return print('Пароль не надежный')
    for i in password:
        if i not in chars and not i.isalnum():
            return print('Пароль не надежный')
    print('Пароль надежный')



x = input()
check_password(x)
