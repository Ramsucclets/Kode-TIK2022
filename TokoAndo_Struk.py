
#Dhama Nanda 12 MIPA /9
x = "Y"
while x=="Y":
    print("""TOKO ANDO
    1.Kremezz Balado  :     Rp. 34.000  
    2.Kremezz BBQ     :     Rp. 32.000
    3.Kremezz Keju    :     Rp. 35.000
    4.Zeky            :     Rp. 10.000
    5.Permen Kaki     :     Rp. 20.000
    """)
    
    h = (input("\nInput Jenis Pesanan  (1-5) :"))
    j = int(input("Input berapa Pesanan : "))
    if h=="1": 
        x=34000
    elif h=="2": 
        x=32000
    elif h=="3": 
        x=35000
    elif h=="4": 
        x=10000
    elif h=="5": 
        x=20000
    total = j*x
    bayar=int(input("Berapa yang anda bayar :"))

    print("""\nTOKO ANDO
    Jl. CEMARA RAYA NO. 73B
    0895411871184
    No Stk  :493668                 ID:ISAH
    Kpd Yth :CASH UMUM
    Tgl     :20/10/2022             Jam:13:58:31
    -----------------------------------------------------------""")
    if h=="1": 
        print(f"Kremezz Balado {j}xPCS Rp.{total}")
    elif h=="2": 
        print(f"Kremezz BBQ {j}xPCS Rp.{total}")
    elif h=="3": 
        print(f"Kremezz Keju {j}xPCS Rp.{total}")
    elif h=="4": 
        print(f"Kremezz Balado {j}xPCS Rp.{total}")
    elif h=="5": 
        print(f"Kremezz Balado {j}xPCS Rp.{total}")
    print("-----------------------------------------------------------")
    print(f"Tot.Item:{j}\t\t Tot.Belanja: Rp.{total}")
    print(f"\t\t\t Total: Rp.{total}")
    print(f"\t\t\t Bayar: Rp.{bayar}")
    Kembali=bayar-total
    print(f"\t\t\t Kembali: Rp.{Kembali}")

    print("\tTermikasih")
x = input("Ulangi lagi ?: [Y/N] ").upper

