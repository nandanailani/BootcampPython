yard = input("Masukkan yard : ")
roll = input("Masukkan roll : ")
uang = input("Masukkan jumlah uang : ")

yard = int(yard)
roll = int(roll)
uang = float(uang)

total_yard = roll * yard
harga_satuan_yard = uang/total_yard
print("Harga yard satuan yang didapat adalah" , harga_satuan_yard, "total yard yang didapat adalah", total_yard)
