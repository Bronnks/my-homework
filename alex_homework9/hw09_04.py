def count_vowels(s: str, case_sensitive: bool = False) -> int:
    count = 0
    vowels = 'aeiou'
    vowels_upper = vowels.upper() + vowels
    res = ''
    if case_sensitive is False:
        for i in s.lower():
            if i in vowels and i not in res:
                count += 1
                res += i
    else:
        for i in s:
            if i in vowels_upper and i not in res:
                count += 1
                res += i

    return count


test = input('Введите строку:')
print(count_vowels(test))
