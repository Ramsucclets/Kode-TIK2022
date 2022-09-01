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

func = int(input())
if func in range(0,4):
    num1 = int(input("First number = "))
    num2 = int(input("Second number = "))
    if func == 1: 
        print(add(num1,num2))
    elif func == 2:
        print(sub(num1,num2))
    elif func == 3: 
        print(mult(num1,num2))
    if func == 4: 
        print(div(num1,num2))
else:
    print("not in range)

