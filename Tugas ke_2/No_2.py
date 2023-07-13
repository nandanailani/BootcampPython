total_liter = float(input("Masukkan Total Liter : "))
ukuran_tahu = float(input("Masukkan Ukuran Tahu (cm) : "))
harga_1_liter_susu = float(input("Masukkan Harga 1 Liter Susu Kedelai : "))
margin_harga_jual = float(input("Margin Harga Jual (%) : "))
alokasi_penjualan = float(input("Alokasi Penjualan (%) : "))

#Konversi liter ke cm^3
volume_susu_kedelai = total_liter * 1000  

# total tahu 
total_tahu = volume_susu_kedelai // ukuran_tahu**3

# sisa susu
sisa_susu = (volume_susu_kedelai - (ukuran_tahu**3 * total_tahu)) / 1000

# total biaya produksi
total_biaya = total_liter * harga_1_liter_susu 

# biaya produksi 1 tahu
biaya_1_tahu = total_biaya / total_tahu

# Harga jual dengan margin
harga_jual = biaya_1_tahu + (biaya_1_tahu * margin_harga_jual / 100)

# Total omset
omset = (total_tahu * harga_jual) * (alokasi_penjualan / 100)

# Total modal
modal = total_tahu * biaya_1_tahu * alokasi_penjualan/100

# Total keuntungan
keuntungan = omset - modal

print("Total tahu yang dihasilkan Sebanyak : {}".format(total_tahu))
print("Sisa Susu Kedelai : {} liter".format(sisa_susu))
print("Total Biaya Produksi : {} Rupiah".format(total_biaya))
print("Biaya Produksi 1 tahu : {} Rupiah".format(("{:.2f}".format(biaya_1_tahu))))
print("Harga jual dengan margin {}% : {:.2f} Rupiah".format(margin_harga_jual, harga_jual))
print("Total Omset : {} Rupiah".format(omset))
print("Total Keuntungan : {:.1f} Rupiah".format(keuntungan))