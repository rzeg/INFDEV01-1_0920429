x = input('Rows and columns ')
for dots in range(1,x):
    if(dots == x - 1):
        print('*' * (x) + " ")
    else:
        print('*' * (x - dots) + " " * (dots - 1) + '*')