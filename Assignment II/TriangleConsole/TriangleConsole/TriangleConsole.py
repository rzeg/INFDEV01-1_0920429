input = input('Rows and columns')

x = input

for dots in range(1,x):
    print('*' * (x - dots) + " " * (dots - 1) + '*')

print('*' * (x) + " ")