color = input()
match color:
    case '(255, 0, 0)':
        print('Red')
    case '(255, 165, 0)':
        print('Orange')
    case '(255, 255, 0)':
        print('Yellow')
    case '(0, 128, 0)':
        print('Green')
    case '(0, 0, 255)':
        print('Blue')
    case '(255, 255, 255)':
        print('White')
    case '(128, 128, 128)':
        print('Gray')
    case _:
        print('Unknown color')
