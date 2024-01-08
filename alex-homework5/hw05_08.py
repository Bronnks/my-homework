alphabet = {
    '.-  ': 'А', '-...': 'Б', '- --': 'В', '--. ': 'Г',
    '-.. ': 'Д', '.   ': 'Е', '...-': 'Ж', '--..': 'З',
    '..  ': 'И', '.---': 'Й', '-.- ': 'К', '.-..': 'Л',
    '--  ': 'М', '-.  ': 'Н', '--- ': 'О', '.--.': 'П',
    '.-. ': 'Р', '... ': 'С', '-   ': 'Т', '..- ': 'У',
    '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч',
    '----': 'Ш', '--.-': 'Щ', '-. -': 'Ъ', '-.--': 'Ы',
    '-..-': 'Ь', '. -.': 'Э', '..--': 'Ю', '.-.-': 'Я',
}
word = input()
chars = '-. '
for i in word:
    if i not in chars:
        word = word.replace(i, '')
morse1 = ''
morse2 = ''
morse3 = ''
start = 0

for i in range(4, len(word) + 1, 4):
    morse1 += f'{alphabet[word[start:i]]}'
    morse2 += '%s' % alphabet[word[start:i]]
    morse3 += '{}'.format(alphabet[word[start:i]])
    start = i

print(morse1, morse2, morse3, sep='\n')
