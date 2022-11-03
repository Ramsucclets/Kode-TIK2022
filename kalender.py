import calendar
yy = 2022
mm = 3
print(calendar.month(yy,mm))

num = int(input('perkalian:'))
for i in range (1,11):
    print(num, '*',i,'=',num*i)

num = int(input('\npembagian:'))
for i in range (1,11):
    print(num, '*',i,'=',num/i)


num = int(input('\nPertambahan:'))
for i in range (1,11):
    print(num, '*',i,'=',num+i)


