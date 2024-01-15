def check_min_max_str(lst):
    min_word = lst[0]
    max_word = lst[0]
    min_len = 1
    max_len = 0
    for i in lst:
        length = len_word(i)
        if length > max_len:
            max_word, max_len = i, length
        elif length <= min_len:
            min_word, min_len = i, length
    print(tuple([min_word, max_word]))


def len_word(wrd):
    count = 0
    for j in range(len(wrd)):
        if wrd[j] != '':
            count += 1
    return count


test1 = input('Введите список слов, через запятую - ').split(',')
check_min_max_str(test1)
