def func(text):
    i = 1
    for sentence in text.split('.'):
        words = sentence.strip().split()
        if not words:
            continue
        res1 = 'Sentence {} has {} words. '.format(i, len(words))
        # res2 = f'Sentence {i} has {len(words)} words. '
        # res3 = 'Sentence %s has %s words. ' % (i, len(words))
        print(res1, end = ' ')
        i += 1
        # print(res2)
        # print(res3)


lst = input()
func(lst)
