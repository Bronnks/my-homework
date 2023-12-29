name, lastname = input().split()
match lastname[-1]:
    case 'а' | 'я':
        print(f'Здравствуйте, госпожа {lastname}')
    case _:
        print(f'Здравствуйте, господин {lastname}')
