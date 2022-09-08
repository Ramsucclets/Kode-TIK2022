from pprint import pp


pilihan="y"
while pilihan=="y":
 print("""
 ===========================================

 12 MIPA Coffee
 List Menu Minuman Kopi 

 ===========================================
 A. Es Kopi Susu : Rp 11.000
 B. Es Kopi Kopi : Rp 12.000
 C. Es Kopi Hitam : Rp 11.000
 D. Ice Americano : Rp 14.000
 ===========================================
 """)
pesan=str(input("masukan list abjad menu kopi= "))
jumlahpesan=int(input("masukan jumlah pesanan="))
if pesan == "a": 
    listnama= "ES Kopi Susu"
    harga=(11000*jumlahpesan)
    ppn=int(harga*0.1)
    if jumlahpesan >= 5: 
        diskon = int(harga*0.2)
        toltalharga=int(harga-diskon+ppn)
    else:
        diskon=(0)
        toltalharga=int(harga+ppn)
elif pesan == "b": 
    listnama= "ES Kopi Coklat"
    harga = (12000*jumlahpesan)
    ppn=int(harga*0.1)