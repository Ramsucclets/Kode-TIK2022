#Judul Program

print("\n\t\tabc")
#Produk dalam toko
print("\nKode Barang \tNama Barang \tNama Barang")
print("k001 \t\tpensil \t\tRp.300")
print("k002 \t\tbuku \t\tRp.500")
print("k003 \t\tkertas \t\tRp.700")
print("k004 \t\tpenghapus \tRp.500")
print("k005 \t\tpenggaris \tRp.1000")

#Variabel
i=1 
#Memasukan banyak belanja
banyakbelanja=int(input("\nMasukan berapa banyak anda ingin belanja :"))
hargabarang =  []
jumlah = []
subtotal = []

#Memasukan kode barang dan jumlah beli
while i <= banyakbelanja:
    h = int(input("\nMasukan harga barang :"))
    j = int(input("Masukan jumlah barang yang ingin dibeli : "))
    s = h*j
    hargabarang.append(h)
    jumlah.append(j)
    subtotal.append(s)
    i = i+1

print(hargabarang, jumlah, subtotal)
