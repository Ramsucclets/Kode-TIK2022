print('Program Python Persegi Panjang Bintang')
print('===========================================================================================')
print()

tinggi_persegi=int(input('Input TP : '))
lebar_persegi=int(input('Input LP :'))
print()

for i in range (tinggi_persegi):
    for j in range(lebar_persegi):
        print(' *',end="")
    print()