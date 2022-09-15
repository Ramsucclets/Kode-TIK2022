ans = "Y"
while ans == "Y":
    nasabah = input("Input nasabah: ")

    print(
"""Pilih Bonus:
1. 15000
2. 22000
3. 45000""")
    bon = int(input("kamu pilih Bonus: "))
    if bon == 1:
        print("1. 15000")
    elif bon == 2:
        print("2. 22000")
    elif bon == 3:
        print("3. 45000")
    else:
        print("salah")
        
    modal = int(input("\nInput Modal\t\t:"))
    sukbuk = float(input("Input Suku bunga\t:"))
    per = int(input("Input Periode\t\t:"))
    per1 = per+1
    
    for i in range(1,per1):
        modal = modal+modal*sukbuk
        print(f"Tahun ke {i}: {modal}")
        
    ans = input("Apakah akan menginput kembali? (Y/N)")
    ans = ans.upper()
    
