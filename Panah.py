#Nama: Dhama Nanda
input("Nama: ")
print("Bentuk/Model : Anak Panah")
for i in range (10):
    for j in range(1):
        print('    *',end="")
    print()

x =4
for i in range(x, 1, -1):
    for space in range(0, x-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()
