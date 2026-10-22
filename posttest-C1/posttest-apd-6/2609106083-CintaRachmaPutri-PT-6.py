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

while program_status == True:
    os.system("cls")

    print(" SISTEM PERSEWAAN ALAT OUTDOOR/CAMPING")
    print("========================================")
    print("1. Login")
    print("2. Register")
    print("3. Keluar dari Program")

    menu_awal = int(input("Pilih menu: "))

    if menu_awal == 1:
        login_count = 3
        login_berhasil = False
        username = ""
        role = ""

        while login_count > 0 and login_berhasil == False:
            print("\n========== LOGIN ==========")
            nama = input("Masukkan username: ")
            password = input("Masukkan password: ")

            login_count -= 1

            if nama in user and password == user[nama]["password"]:
                login_berhasil = True
                username = nama
                role = user[nama]["role"]

            if login_berhasil == True:
                print("\nLogin berhasil")
                print("Selamat datang", username)
                print("Role anda adalah", role)
            else:
                print("Username atau password salah")
                if login_count > 0:
                    print("Login tersisa:", login_count, "kali")

        if login_berhasil == False:
            print("\nKesempatan login habis")
            input("Tekan Enter untuk kembali...")
        else:
            logout = False

            if role == "admin":
                while program_status == True and logout == False:
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

                    print("\n========== MENU ADMIN ==========")
                    print("1. Tambah Alat")
                    print("2. Lihat Semua Penyewaan")
                    print("3. Update Pengembalian")
                    print("4. Hapus Alat Rusak/Hilang")
                    print("5. Logout")
                    print("6. Keluar dari Program")

                    menu = int(input("Pilih menu: "))

                    if menu == 1:
                        nama_alat = input("Masukkan nama alat: ")

                        if nama_alat in alat:
                            print("Nama alat sudah tersedia")
                        else:
                            kategori = input("Masukkan kategori alat: ")
                            harga = int(input("Masukkan harga sewa per hari: "))
                            stok = int(input("Masukkan jumlah stok: "))

                            alat[nama_alat] = {
                                "kategori": kategori,
                                "harga": harga,
                                "stok": stok
                            }

                            print("Alat berhasil ditambahkan")

                    elif menu == 2:
                        print("\n========== DAFTAR PENYEWAAN ==========")
                        print("No | Penyewa | Kontak | Alat | Jumlah | Hari | Total | Status")

                        if len(penyewaan) == 0:
                            print("Belum ada penyewaan")
                        else:
                            for nomor in penyewaan:
                                data = penyewaan[nomor]
                                print(
                                    nomor, "|",
                                    data["nama_penyewa"], "|",
                                    data["kontak"], "|",
                                    data["nama_alat"], "|",
                                    data["jumlah"], "|",
                                    data["hari"], "|",
                                    "Rp.", data["total"], "|",
                                    data["status"]
                                )

                    elif menu == 3:
                        for nomor in penyewaan:
                            data = penyewaan[nomor]
                            print(
                                nomor, "|",
                                data["nama_penyewa"], "|",
                                data["nama_alat"], "|",
                                "Jumlah:", data["jumlah"], "|",
                                "Status:", data["status"]
                            )

                        if len(penyewaan) > 0:
                            nomor = int(input("Nomor penyewaan yang dikembalikan: "))

                            if nomor in penyewaan:
                                if penyewaan[nomor]["status"] == "Disewa":
                                    nama_alat = penyewaan[nomor]["nama_alat"]
                                    jumlah = penyewaan[nomor]["jumlah"]
                                    alat[nama_alat]["stok"] += jumlah
                                    penyewaan[nomor]["status"] = "Dikembalikan"
                                    print("Pengembalian berhasil")
                                else:
                                    print("Alat sudah dikembalikan")
                            else:
                                print("Nomor penyewaan tidak valid")
                        else:
                            print("Belum ada penyewaan")

                    elif menu == 4:
                        i = 1
                        for nama_alat in alat:
                            print(i, "|", nama_alat, "|", alat[nama_alat]["kategori"])
                            i += 1

                        nomor_alat = int(input("Nomor alat yang ingin dihapus: "))
                        nama_terpilih = ""
                        i = 1

                        for nama_alat in alat:
                            if i == nomor_alat:
                                nama_terpilih = nama_alat
                            i += 1

                        if nama_terpilih != "":
                            sedang_disewa = False

                            for nomor in penyewaan:
                                if (
                                    penyewaan[nomor]["nama_alat"] == nama_terpilih
                                    and penyewaan[nomor]["status"] == "Disewa"
                                ):
                                    sedang_disewa = True

                            if sedang_disewa == False:
                                print("1. Rusak")
                                print("2. Hilang")
                                alasan = int(input("Pilih alasan penghapusan: "))

                                if alasan == 1 or alasan == 2:
                                    del alat[nama_terpilih]
                                    print("Data alat berhasil dihapus")
                                else:
                                    print("Pilihan tidak valid")
                            else:
                                print("Alat masih disewa dan belum dikembalikan")
                        else:
                            print("Nomor alat tidak valid")

                    elif menu == 5:
                        logout = True
                        os.system("cls")
                        print("Logout berhasil")

                    elif menu == 6:
                        program_status = False
                        logout = True
                        os.system("cls")
                        print("Program selesai")

                    else:
                        print("Menu tidak valid")

                    if logout == False and program_status == True:
                        input("\nTekan Enter untuk melanjutkan.")
                        os.system("cls")

            elif role == "pengguna":
                while program_status == True and logout == False:
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

                    print("\n========== MENU PENGGUNA ==========")
                    print("1. Sewa Alat")
                    print("2. Lihat Penyewaan Saya")
                    print("3. Kembalikan Alat")
                    print("4. Logout")
                    print("5. Keluar dari Program")

                    menu = int(input("Pilih menu: "))

                    if menu == 1:
                        nomor_alat = int(input("Pilih nomor alat yang disewa: "))
                        nama_terpilih = ""
                        i = 1

                        for nama_alat in alat:
                            if i == nomor_alat:
                                nama_terpilih = nama_alat
                            i += 1

                        if nama_terpilih != "":
                            if alat[nama_terpilih]["stok"] > 0:
                                nama_penyewa = input("Masukkan nama penyewa: ")
                                kontak = input("Masukkan nomor HP: ")
                                jumlah = int(input("Masukkan jumlah alat: "))
                                hari = int(input("Masukkan lama sewa (hari): "))

                                if (
                                    jumlah > 0
                                    and jumlah <= alat[nama_terpilih]["stok"]
                                    and hari > 0
                                ):
                                    total = alat[nama_terpilih]["harga"] * jumlah * hari

                                    print("\n========== KONFIRMASI SEWA ==========")
                                    print("Nama penyewa:", nama_penyewa)
                                    print("Nama alat:", nama_terpilih)
                                    print("Jumlah:", jumlah)
                                    print("Lama sewa:", hari, "hari")
                                    print("Total harga: Rp.", total)

                                    konfirmasi = input("Lanjutkan? (y/n): ")

                                    if konfirmasi == "y" or konfirmasi == "Y":
                                        penyewaan[nomor_penyewaan_baru] = {
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

                                        nomor_penyewaan_baru += 1
                                    else:
                                        print("Penyewaan dibatalkan")
                                else:
                                    print("Jumlah atau lama sewa tidak valid")
                            else:
                                print("Stok alat habis")
                        else:
                            print("Nomor alat tidak valid")

                    elif menu == 2:
                        ada_pesanan = False
                        print("\n========== PENYEWAAN SAYA ==========")

                        for nomor in penyewaan:
                            data = penyewaan[nomor]
                            if data["username"] == username:
                                ada_pesanan = True
                                print(
                                    nomor, "|",
                                    data["nama_penyewa"], "|",
                                    data["nama_alat"], "|",
                                    "Jumlah:", data["jumlah"], "|",
                                    "Hari:", data["hari"], "|",
                                    "Total: Rp.", data["total"], "|",
                                    "Status:", data["status"]
                                )

                        if ada_pesanan == False:
                            print("Belum ada penyewaan")

                    elif menu == 3:
                        ada_pesanan = False

                        for nomor in penyewaan:
                            data = penyewaan[nomor]
                            if data["username"] == username and data["status"] == "Disewa":
                                ada_pesanan = True
                                print(
                                    nomor, "|",
                                    data["nama_alat"], "|",
                                    "Jumlah:", data["jumlah"]
                                )

                        if ada_pesanan == True:
                            nomor = int(input("Nomor penyewaan yang dikembalikan: "))

                            if nomor in penyewaan:
                                if penyewaan[nomor]["username"] == username:
                                    if penyewaan[nomor]["status"] == "Disewa":
                                        nama_alat = penyewaan[nomor]["nama_alat"]
                                        jumlah = penyewaan[nomor]["jumlah"]
                                        alat[nama_alat]["stok"] += jumlah
                                        penyewaan[nomor]["status"] = "Dikembalikan"
                                        print("Pengembalian berhasil")
                                    else:
                                        print("Alat sudah dikembalikan")
                                else:
                                    print("Penyewaan tersebut bukan milik kamu")
                            else:
                                print("Nomor penyewaan tidak valid")
                        else:
                            print("Tidak ada alat yang perlu dikembalikan")

                    elif menu == 4:
                        logout = True
                        os.system("cls")
                        print("Logout berhasil")

                    elif menu == 5:
                        program_status = False
                        logout = True
                        os.system("cls")
                        print("Program selesai")

                    else:
                        print("Menu tidak valid")

                    if logout == False and program_status == True:
                        input("\nTekan Enter untuk melanjutkan.")
                        os.system("cls")

    elif menu_awal == 2:
        os.system("cls")
        print("========== REGISTER ==========")

        nama_baru = input("Masukkan username baru: ")
        username_ada = nama_baru in user

        if nama_baru == "":
            print("Username tidak boleh kosong")
        elif username_ada == True:
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

        input("\nTekan Enter untuk kembali ke menu utama.")

    elif menu_awal == 3:
        program_status = False
        os.system("cls")
        print("Program selesai. Terima kasih!")
    else:
        print("Menu tidak valid")

