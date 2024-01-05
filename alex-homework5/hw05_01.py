number = input()
print(f'+375 ({number[2:4]}) {number[4:7]}-{number[7:9]}-{number[9:]}')
print('+375 (%s) %s-%s-%s' % (number[2:4], number[4:7], number[7:9], number[9:]))
print('+375 ({}) {}-{}-{}'.format(number[2:4], number[4:7], number[7:9], number[9:]))
