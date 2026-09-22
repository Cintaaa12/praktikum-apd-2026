# Deklarasi harga komponen
komponen_1 = 120000
komponen_2 = 135000
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000

biaya_admin = 15000

# Memasukkan isi komponen ke dalam list
harga_komponen = [komponen_1, komponen_2, komponen_3, komponen_4, komponen_5, komponen_6]

# Hitung total biaya secara manual (tanpa fungsi sum())
total_biaya = komponen_1 + komponen_2 + komponen_3 + komponen_4 + komponen_5 + komponen_6 + biaya_admin

# Hitung rata-rata menggunakan len()
rata_rata = total_biaya / len(harga_komponen)

# Nim = 83

# Variabel bolean
bolean = 83 != rata_rata

# Konversikan total_biaya ke GBP (asumsi kurs 1 GBP = Rp20.500)
kurs_gbp = 20500
total_biaya_gbp = total_biaya / kurs_gbp

# Menampilkan semua variabel
print("=== HASIL PERHITUNGAN ===")
print("Daftar Harga Komponen :", harga_komponen)
print("Total Biaya           : Rp", total_biaya)
print("Rata-rata             :", rata_rata)
print("NIM                   :", 83)
print("Bolean (NIM != Rata)  :", bolean)
print("Total Biaya (GBP)     : £", round(total_biaya_gbp, 2))
print("Komponen 1 s.d. 4     :", harga_komponen[-6:-2])
