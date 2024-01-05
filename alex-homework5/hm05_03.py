lst = input().split('. ')

for i in range(len(lst)):
    # print('Sentence {} has {} words.'.format(i+1, len(lst[i].split())), end=' ')
    # print(f'Sentence {i+1} has {len(lst[i].split())} words.', end = ' ')
    print('Sentence %s has %s words.' % (i + 1, len(lst[i].split())), end=' ')
