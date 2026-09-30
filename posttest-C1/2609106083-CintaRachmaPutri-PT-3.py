nickname = "cinta"
nim = "83"

print("=== SISTEM TOP UP GAME ===")
nama = input ("Masukkan nama mu : ").lower()
nim = input("Masukkan 2 digit terakhir NIM : ")

login = nama == nickname and nim == nim
if not login:
    print("\nLogin Gagal")
    exit()

print("\nLogin Berhasil \nSelamat Datang Kembali")

print("=== FORM TOP UP GAME ===")
id_player = input("Masukkan ID Player : ")
nama_game = input("Masukkan Nama Game (Genshin Impact / Minecraft / Mobile Legends) : ")
kategori_topup = input("Masukkan Kategori Top Up (Kecil / Menengah / Besar) : ")
metode_pembayaran = input("Masukkan Metode Pembayaran (Pulsa / E-Wallet) : ")

kategori_clean = kategori_topup.strip().lower()
if kategori_clean == "kecil" :
    harga_dasar = 15000
elif kategori_clean == "menengah" :
    harga_dasar = 50000
elif kategori_clean == "besar" :
    harga_dasar = 150000
else:
    harga_dasar = 0
    print("\nPilihannya kecil/menengah/besar")
    exit()

metode_clean = metode_pembayaran.strip().lower()
biaya_admin = 2500 

total_bayar = harga_dasar + biaya_admin

print("\n===== STRUK PEMBELIAN =====")
print(f"ID Player        : {"id_player"}")
print(f"Nama Game        : {"nama_game"}")
print(f"Kategori Top Up  : {"kategori_topup"}")
print(f"Metode Pembayran : {"metode_pembayaran"}")
print(f"Harga Dasar      : Rp {"harga_dasar"}")
print(f"Biaya Admin      : Rp {"biaya_admin"}")
print("-----------------------------")
print(f"Total Bayar      : Rp {"total_bayar"}")
print("=============================")