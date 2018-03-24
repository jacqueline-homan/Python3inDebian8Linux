#!/usr/bin/python3

# Nota Bene: to run this in terminal, use the command
# python3.6m instead of python or python3 or
# the program won't work - you'll get an invalid syntax error.

x = 0x0a
y = 0x02
z = x & y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')


