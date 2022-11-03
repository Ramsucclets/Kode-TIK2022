print(""" \t TOKO DINGIN
1.Nasi Dingin     :     Rp. 5.000  
2.Mie Dingin      :     Rp. 11.000
3.Ayam Dingin     :     Rp. 99.000
4.Teh Botol Panas :     Rp. 89.000
5.Meja            :     Rp. 33.000
6.Jendela         :     Rp. 727.000
""")

h = (input("\nInput Jenis Pesanan :"))
j = int(input("Input berapa Pesanan: "))
if h=="1": 
    x=5000
elif h=="2": 
    x=11000
elif h=="3": 
    x=99000
elif h=="4": 
    x=89000
elif h=="5": 
    x=33000
elif h=="6": 
    x=727000
total = j*x
print("Total : ", total)
Bayar = int(input("Input uang pemabayaran: "))
Kembali =total-Bayar
print("Kembali :", Kembali)