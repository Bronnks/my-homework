binary = int(input(), 2)
print(f'Decimal: {binary}, Octal: {binary:o}, Hexadecimal: {binary:X}.')
print('Decimal: %d, Octal: %o, Hexadecimal: %X.' % (binary, binary, binary))
print('Decimal: {0:d}, Octal: {0:o}, Hexadecimal: {0:X}.'.format(binary))
