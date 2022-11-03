print('1')
a = 5
for i in range (0,a):
    for j in range(0,i+1):
        print('*',end='')
    print ('')


print('\n\n2')
a=6
for i in range (0,a):
    for j in range (0,a-1):
        print('*',end='')
    a=1
    print('')

print('3')
a = 6
k = 0
for i in range(1, a+1):
    for space in range(1, (a-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()

print('4')
x = 6
for i in range(x, 1, -1):
    for space in range(0, x-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()