import os

user = {
    "admin": {"password": "admin123", "role": "admin"},
    "cinta": {"password": "cinta", "role": "pengguna"}
}

alat = {
    "Tenda": {"kategori": "Tempat Tidur", "harga": 50000, "stok": 5},
    "Sleeping Bag": {"kategori": "Perlengkapan Tidur", "harga": 15000, "stok": 10},
    "Carrier": {"kategori": "Tas Gunung", "harga": 25000, "stok": 8},
    "Kompor Portable": {"kategori": "Memasak", "harga": 20000, "stok": 6},
    "Matras": {"kategori": "Perlengkapan Tidur", "harga": 10000, "stok": 10},
    "Headlamp": {"kategori": "Penerangan", "harga": 10000, "stok": 8}
}

penyewaan = {}
nomor_penyewaan_baru = 1
program_status = True

def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def tampilkan_daftar_alat():
    print("\n========== DAFTAR ALAT ==========")
    print("No | Nama Alat | Kategori | Harga/Hari | Stok")

    i = 1
    for nama_alat in alat:
        print(
            i, "|",
            nama_alat, "|",
            alat[nama_alat]["kategori"], "|",
            "Rp.", alat[nama_alat]["harga"], "|",
            alat[nama_alat]["stok"]
        )
        i += 1


def tampilkan_penyewaan(filter_username):
    ada_data = False

    for nomor in penyewaan:
        data = penyewaan[nomor]
        if filter_username == "" or data["username"] == filter_username:
            ada_data = True
            print(
                nomor, "|",
                data["nama_penyewa"], "|",
                data["kontak"], "|",
                data["nama_alat"], "|",
                "Jumlah:", data["jumlah"], "|",
                "Hari:", data["hari"], "|",
                "Total: Rp.", data["total"], "|",
                "Status:", data["status"]
            )

    if ada_data == False:
        print("Belum ada penyewaan")

    return ada_data

def ambil_nomor_penyewaan():
    global nomor_penyewaan_baru
    nomor = nomor_penyewaan_baru
    nomor_penyewaan_baru += 1
    return nomor


def input_nomor_hp():
    while True:
        try:
            kontak = input("Masukkan nomor HP: ")
            if kontak.isdigit() == False:
                raise ValueError("Nomor HP hanya boleh berisi angka")
            if len(kontak) < 10 or len(kontak) > 13:
                raise ValueError("Nomor HP harus 10 sampai 13 digit")
            return kontak
        except ValueError as pesan_error:
            print("Error:", pesan_error)

def input_angka(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            return nilai
        except ValueError:
            print("Error: input harus berupa angka bulat")


def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Error: input tidak boleh kosong")
        else:
            return teks


def hitung_total(harga, jumlah, hari):
    return harga * jumlah * hari


def cari_nama_alat(nomor_alat):
    nama_terpilih = ""
    i = 1

    for nama_alat in alat:
        if i == nomor_alat:
            nama_terpilih = nama_alat
        i += 1

    return nama_terpilih


def cek_sedang_disewa(nama_alat):
    for nomor in penyewaan:
        if penyewaan[nomor]["nama_alat"] == nama_alat and penyewaan[nomor]["status"] == "Disewa":
            return True
    return False


def hitung_stok_rekursif(daftar_nama, indeks):
    if indeks == len(daftar_nama):
        return 0
    stok_sekarang = alat[daftar_nama[indeks]]["stok"]
    return stok_sekarang + hitung_stok_rekursif(daftar_nama, indeks + 1)


def proses_login(sisa_kesempatan):
    if sisa_kesempatan == 0:
        return ""

    print("\n========== LOGIN ==========")
    nama = input("Masukkan username: ")
    password = input("Masukkan password: ")

    try:
        if password == user[nama]["password"]:
            return nama
        print("Username atau password salah")
    except KeyError:
        print("Username atau password salah")

    if sisa_kesempatan - 1 > 0:
        print("Login tersisa:", sisa_kesempatan - 1, "kali")

    return proses_login(sisa_kesempatan - 1)

def register():
    print("========== REGISTER ==========")

    nama_baru = input("Masukkan username baru: ").strip()

    if nama_baru == "":
        print("Username tidak boleh kosong")
    elif nama_baru in user:
        print("Username sudah digunakan")
    else:
        password_baru = input("Masukkan password baru: ")

        if password_baru == "":
            print("Password tidak boleh kosong")
        else:
            user[nama_baru] = {
                "password": password_baru,
                "role": "pengguna"
            }
            print("Registrasi berhasil")
            print("Silakan login menggunakan akun baru")


def tambah_alat():
    nama_alat = input_teks("Masukkan nama alat: ")

    if nama_alat in alat:
        print("Nama alat sudah tersedia")
        return

    kategori = input_teks("Masukkan kategori alat: ")
    harga = input_angka("Masukkan harga sewa per hari: ")
    stok = input_angka("Masukkan jumlah stok: ")

    if harga <= 0 or stok < 0:
        print("Harga harus lebih dari 0 dan stok tidak boleh negatif")
        return

    alat[nama_alat] = {
        "kategori": kategori,
        "harga": harga,
        "stok": stok
    }
    print("Alat berhasil ditambahkan")


def hapus_alat():
    i = 1
    for nama_alat in alat:
        print(i, "|", nama_alat, "|", alat[nama_alat]["kategori"])
        i += 1

    nomor_alat = input_angka("Nomor alat yang ingin dihapus: ")
    nama_terpilih = cari_nama_alat(nomor_alat)

    if nama_terpilih == "":
        print("Nomor alat tidak valid")
    elif cek_sedang_disewa(nama_terpilih) == True:
        print("Alat masih disewa dan belum dikembalikan")
    else:
        print("1. Rusak")
        print("2. Hilang")
        alasan = input_angka("Pilih alasan penghapusan: ")

        if alasan == 1 or alasan == 2:
            try:
                del alat[nama_terpilih]
                print("Data alat berhasil dihapus")
            except KeyError:
                print("Data alat tidak ditemukan")
        else:
            print("Pilihan tidak valid")


def sewa_alat(username):
    nomor_alat = input_angka("Pilih nomor alat yang disewa: ")
    nama_terpilih = cari_nama_alat(nomor_alat)

    if nama_terpilih == "":
        print("Nomor alat tidak valid")
        return

    if alat[nama_terpilih]["stok"] <= 0:
        print("Stok alat habis")
        return

    nama_penyewa = input_teks("Masukkan nama penyewa: ")
    kontak = input_nomor_hp()
    jumlah = input_angka("Masukkan jumlah alat: ")
    hari = input_angka("Masukkan lama sewa (hari): ")

    if jumlah <= 0 or jumlah > alat[nama_terpilih]["stok"] or hari <= 0:
        print("Jumlah atau lama sewa tidak valid")
        return

    total = hitung_total(alat[nama_terpilih]["harga"], jumlah, hari)

    print("\n========== KONFIRMASI SEWA ==========")
    print("Nama penyewa:", nama_penyewa)
    print("Nama alat:", nama_terpilih)
    print("Jumlah:", jumlah)
    print("Lama sewa:", hari, "hari")
    print("Total harga: Rp.", total)

    konfirmasi = input("Lanjutkan? (y/n): ")

    if konfirmasi == "y" or konfirmasi == "Y":
        nomor = ambil_nomor_penyewaan()
        penyewaan[nomor] = {
            "nama_penyewa": nama_penyewa,
            "kontak": kontak,
            "nama_alat": nama_terpilih,
            "jumlah": jumlah,
            "hari": hari,
            "total": total,
            "status": "Disewa",
            "username": username
        }

        alat[nama_terpilih]["stok"] -= jumlah
        print("Penyewaan berhasil")
        print("Sisa stok:", alat[nama_terpilih]["stok"])
    else:
        print("Penyewaan dibatalkan")


def proses_pengembalian(username, role):
    print("\n========== DAFTAR YANG BELUM DIKEMBALIKAN ==========")
    ada_pesanan = False

    for nomor in penyewaan:
        data = penyewaan[nomor]
        if data["status"] == "Disewa" and (role == "admin" or data["username"] == username):
            ada_pesanan = True
            print(nomor, "|", data["nama_penyewa"], "|", data["nama_alat"], "|", "Jumlah:", data["jumlah"])

    if ada_pesanan == False:
        print("Tidak ada alat yang perlu dikembalikan")
        return

    nomor = input_angka("Nomor penyewaan yang dikembalikan: ")

    try:
        data = penyewaan[nomor]

        if role != "admin" and data["username"] != username:
            print("Penyewaan tersebut bukan milik kamu")
        elif data["status"] != "Disewa":
            print("Alat sudah dikembalikan")
        else:
            alat[data["nama_alat"]]["stok"] += data["jumlah"]
            data["status"] = "Dikembalikan"
            print("Pengembalian berhasil")
    except KeyError:
        print("Nomor penyewaan tidak valid atau data alat sudah dihapus")

def menu_admin():
    global program_status
    logout = False

    while program_status == True and logout == False:
        tampilkan_daftar_alat()

        print("\n========== MENU ADMIN ==========")
        print("1. Tambah Alat")
        print("2. Lihat Semua Penyewaan")
        print("3. Update Pengembalian")
        print("4. Hapus Alat Rusak/Hilang")
        print("5. Lihat Total Stok")
        print("6. Logout")
        print("7. Keluar dari Program")

        menu = input_angka("Pilih menu: ")

        if menu == 1:
            tambah_alat()
        elif menu == 2:
            print("\n========== DAFTAR PENYEWAAN ==========")
            tampilkan_penyewaan("")
        elif menu == 3:
            proses_pengembalian("admin", "admin")
        elif menu == 4:
            hapus_alat()
        elif menu == 5:
            total_stok = hitung_stok_rekursif(list(alat.keys()), 0)
            print("Total seluruh stok alat:", total_stok)
        elif menu == 6:
            logout = True
            bersihkan_layar()
            print("Logout berhasil")
        elif menu == 7:
            program_status = False
            logout = True
            bersihkan_layar()
            print("Program selesai")
        else:
            print("Menu tidak valid")

        if logout == False and program_status == True:
            input("\nTekan Enter untuk melanjutkan.")
            bersihkan_layar()


def menu_pengguna(username):
    global program_status
    logout = False

    while program_status == True and logout == False:
        tampilkan_daftar_alat()

        print("\n========== MENU PENGGUNA ==========")
        print("1. Sewa Alat")
        print("2. Lihat Penyewaan Saya")
        print("3. Kembalikan Alat")
        print("4. Logout")
        print("5. Keluar dari Program")

        menu = input_angka("Pilih menu: ")

        if menu == 1:
            sewa_alat(username)
        elif menu == 2:
            print("\n========== PENYEWAAN SAYA ==========")
            tampilkan_penyewaan(username)
        elif menu == 3:
            proses_pengembalian(username, "pengguna")
        elif menu == 4:
            logout = True
            bersihkan_layar()
            print("Logout berhasil")
        elif menu == 5:
            program_status = False
            logout = True
            bersihkan_layar()
            print("Program selesai")
        else:
            print("Menu tidak valid")

        if logout == False and program_status == True:
            input("\nTekan Enter untuk melanjutkan.")
            bersihkan_layar()


def menu_login():
    username = proses_login(3)

    if username == "":
        print("\nKesempatan login habis")
        input("Tekan Enter untuk kembali...")
        return

    role = user[username]["role"]
    print("\nLogin berhasil")
    print("Selamat datang", username)
    print("Role anda adalah", role)

    if role == "admin":
        menu_admin()
    else:
        menu_pengguna(username)

def main():
    global program_status

    while program_status == True:
        bersihkan_layar()

        print(" SISTEM PERSEWAAN ALAT OUTDOOR/CAMPING")
        print("========================================")
        print("1. Login")
        print("2. Register")
        print("3. Keluar dari Program")

        menu_awal = input_angka("Pilih menu: ")

        if menu_awal == 1:
            menu_login()
        elif menu_awal == 2:
            bersihkan_layar()
            register()
            input("\nTekan Enter untuk kembali ke menu utama.")
        elif menu_awal == 3:
            program_status = False
            bersihkan_layar()
            print("Program selesai. Terima kasih!")
        else:
            print("Menu tidak valid")
            input("\nTekan Enter untuk melanjutkan.")

main()