#fungsi penjumlahan
from re import X
from wsgiref.validate import InputWrapper


def add(x,y):
    return x+y
#fungsi pengurangan
def subtract(x,y):
    return x-y
#fungsi perkalian 
def multiply(x,y):
    return x*y
#fungsi pembagian 
def divide (x, y):
    return x/y
#menu operasi 
print('Pilihan Operasi')
print('1.Jumlah')
print('2.Kurang')
print('3.Kali')
print('4.Bagi')

a = int(input('\n'))
num1 = int(input("masukan angka pertama: ")) 
num2 = int(input("masukan angka kedua: "))

if a == '1':
    print(add(num1,num2))
elif a == '2': 
    print(subtract(num1,num2))
elif a == '3':
    print(multiply)
elif a == '4': 
    print(divide)

