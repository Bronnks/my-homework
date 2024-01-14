from collections import Counter

def func(text):
    text = text.split('.')
    count = 1
    for i in range(len(text)):

        c = Counter(text[i].split())
        if len(c) == 0:
            continue
        print(f'Sentence {count} has {len(c)} words.', end=' ')
        count +=1


for i in ['', ' ', ' . ', 'Sentence', 'Sentence 2', 'Sentence 3.', 'Sentence 4. Sentence']:
    func(i)