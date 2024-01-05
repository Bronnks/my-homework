lst = input().split('. ')
res1, res2, res3 = '', '', ''
for i in range(len(lst)):
    res1 += 'Sentence {} has {} words. '.format(i + 1, len(lst[i].split()))
    res2 += f'Sentence {i + 1} has {len(lst[i].split())} words. '
    res3 += 'Sentence %s has %s words. ' % (i + 1, len(lst[i].split()))

print(res1, res2, res3, sep='\n')
