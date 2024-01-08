alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = input('Введите слово для шифрования - ').upper()
step = int(input('Введите шаг шифрования - '))
caesar = ''
for i in password:
    caesar += alphabet[alphabet.find(i) - 26 + step]
print(f'Шифрованное слово - {caesar.lower()}')

print('А теперь дешифруем')

caesar = input('Введите шифрованное слово - ').upper()
step = int(input('Введите шаг шифрования - '))
password = ''
for i in caesar:
    password += alphabet[alphabet.find(i) - step]
print(f'Зашифровано было - {password.lower()}')
