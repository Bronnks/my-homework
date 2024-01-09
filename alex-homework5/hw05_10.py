word = input()

match word[-1]:
    case 's' | 'x' | 'z':
        word += 'es'
    case 'h':
        if word[-2] in 'cs':
            word += 'es'
        else:
            word += 's'
    case 'y':
        if word[-2] not in 'aeiouy':
            word = word[:-1] + 'ies'
        else:
            word += 's'
    case _:
        word += 's'
print(word)
