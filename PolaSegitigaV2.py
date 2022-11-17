
#Dhama Nanda 12 MIPA
a = 6
k = 0
for i in range(1, a+1):
    for space in range(1, (a-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print(" >x ", end="")
        k += 1
    k = 0
    print()
    x=6
print(' ')
z=5
for i in range(z):
    print(" "*(z-i), end="")
    print("="*i, end="")
    print("+"*(i+1), end="")
    print(" "*(z-i-1), end="")
    print(" "*(z-i), end="")
    print("{"*i, end="")
    print("}"*(i+1), end="")
    print()
for i in range(z):
    print(" "*(i+1), end="")
    print(">"*(z-1-i), end="")
    print("|" * (z - i), end="")
    print(" "*(i), end="")
    print(" "*(i+1), end="")
    print(";"*(z-1-i), end="")
    print("&" * (z - i), end="")
    print()
for i in range(z):
    print(" "*(z-i), end="")
    print("&"*i, end="")
    print("$"*(i+1), end="")
    print(" "*(z-i-1), end="")
    print(" "*(z-i), end="")
    print("!"*i, end="")
    print("@"*(i+1), end="")


    print()
for i in range(z):
    print(" "*(i+1), end="")
    print("."*(z-1-i), end="")
    print("<" * (z - i), end="")
    print(" "*(i), end="")
    print(" "*(i+1), end="")
    print("`"*(z-1-i), end="")
    print("~" * (z - i), end="")

    print()
for i in range(x, 1, -1):
    for space in range(0, x-i):
        print("  ", end=" ")
    for j in range(i, 2*i-1):
        print(" _ ", end=" ")
    for j in range(1, i-1):
        print(" x ", end=" ")
    print()

