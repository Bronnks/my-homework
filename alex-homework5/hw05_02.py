# вариант когда слов больше двух
some_words = input('введите несколько слов - ').split()
rev = ' '.join(some_words[::-1])
print(f'{rev}')
print('%s' % rev)
print('{}'.format(rev))

# вариант когда слов всего два
word1, word2 = input('введите два слова - ').split()
print(f'{word2} {word1}')
print('%s %s' % (word2, word1))
print('{1} {0}'.format(word1, word2))
 
# rev = input().split()
# print('{} {}'.format(rev[1], rev[0]))
# print(f'{rev[1]} {rev[0]}')
# print('%s %s' % (rev[1], rev[0]))
