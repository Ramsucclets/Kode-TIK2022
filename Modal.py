print('Nilai Masa Depan')
print('============================\n')
modal = float(input('Masukan modal awal anda = Rp.'))
suku = float(input('Masukan suku bunga yang ditawarkan (dalam desimal) ='))
waktu = int(input('Lama penamaan modal anda(dalam tahun ) = '))
for i in range (1,waktu+1,1):
    modal *= (1+suku)
    print(f'Modal tahun ke- {i} Anda adalah = Rp.',modal )
