from collections import Counter
lst = input().split('. ')
cnt = Counter()
for i in range(len(lst)):
    cnt[i] = len(lst[i].split())
for key, value in cnt.items():
    print(f'Sentence {key+1} has {value} words.', end = ' ')