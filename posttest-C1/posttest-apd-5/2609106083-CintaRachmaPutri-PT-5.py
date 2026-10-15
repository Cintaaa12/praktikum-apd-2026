import os

user = [
    ["admin", "admin123", "admin"],
    ["cinta", "cinta", "pengguna"]
]

alat = [
    ["Tenda", "Tempat Tidur", 50000, 5],
    ["Sleeping Bag", "Perlengkapan Tidur", 15000, 10],
    ["Carrier", "Tas Gunung", 25000, 8],
    ["Kompor Portable", "Memasak", 20000, 6],
    ["Matras", "Perlengkapan Tidur", 10000, 10],
    ["Headlamp", "Penerangan", 10000, 8]
]
penyewaan = []

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

            for i in range(len(user)):
                if nama == user[i][0] and password == user[i][1]:
                    login_berhasil = True
                    username = user[i][0]
                    role = user[i][2]
                    break

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

                    for i in range(len(alat)):
                        print(
                            i + 1, "|",
                            alat[i][0], "|",
                            alat[i][1], "|",
                            "Rp.", alat[i][2], "|",
                            alat[i][3]
                        )

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
                        kategori = input("Masukkan kategori alat: ")
                        harga = int(input("Masukkan harga sewa per hari: "))
                        stok = int(input("Masukkan jumlah stok: "))

                        alat.append([
                            nama_alat,
                            kategori,
                            harga,
                            stok
                        ])

                        print("Alat berhasil ditambahkan")

                    elif menu == 2:
                        print("\n========== DAFTAR PENYEWAAN ==========")
                        print("No | Penyewa | Kontak | Alat | Jumlah | Hari | Total | Status")

                        for i in range(len(penyewaan)):
                            print(
                                i + 1, "|",
                                penyewaan[i][0], "|",
                                penyewaan[i][1], "|",
                                penyewaan[i][2], "|",
                                penyewaan[i][3], "|",
                                penyewaan[i][4], "|",
                                "Rp.", penyewaan[i][5], "|",
                                penyewaan[i][6]
                            )

                        if len(penyewaan) == 0:
                            print("Belum ada penyewaan")

                    elif menu == 3:
                        for i in range(len(penyewaan)):
                            print(
                                i + 1, "|",
                                penyewaan[i][0], "|",
                                penyewaan[i][2], "|",
                                "Jumlah:", penyewaan[i][3], "|",
                                "Status:", penyewaan[i][6]
                            )

                        if len(penyewaan) > 0:
                            nomor = int(input("Nomor penyewaan yang dikembalikan: "))

                            if nomor > 0 and nomor <= len(penyewaan):
                                indeks = nomor - 1

                                if penyewaan[indeks][6] == "Disewa":
                                    for i in range(len(alat)):
                                        if alat[i][0] == penyewaan[indeks][2]:
                                            alat[i][3] += penyewaan[indeks][3]
                                            break

                                    penyewaan[indeks][6] = "Dikembalikan"
                                    print("Pengembalian berhasil")
                                else:
                                    print("Alat sudah dikembalikan")
                            else:
                                print("Nomor penyewaan tidak valid")
                        else:
                            print("Belum ada penyewaan")

                    elif menu == 4:
                        nomor = int(input("Nomor alat yang ingin dihapus: "))

                        if nomor > 0 and nomor <= len(alat):
                            indeks = nomor - 1
                            sedang_disewa = False

                            for i in range(len(penyewaan)):
                                if (
                                    penyewaan[i][2] == alat[indeks][0]
                                    and penyewaan[i][6] == "Disewa"
                                ):
                                    sedang_disewa = True

                            if sedang_disewa == False:
                                print("1. Rusak")
                                print("2. Hilang")
                                alasan = int(input("Pilih alasan penghapusan: "))

                                if alasan == 1 or alasan == 2:
                                    alat.pop(indeks)
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

            elif role == "pengguna":
                while program_status == True and logout == False:
                    print("\n========== DAFTAR ALAT ==========")
                    print("No | Nama Alat | Kategori | Harga/Hari | Stok")

                    for i in range(len(alat)):
                        print(
                            i + 1, "|",
                            alat[i][0], "|",
                            alat[i][1], "|",
                            "Rp.", alat[i][2], "|",
                            alat[i][3]
                        )

                    print("\n========== MENU PENGGUNA ==========")
                    print("1. Sewa Alat")
                    print("2. Lihat Penyewaan Saya")
                    print("3. Kembalikan Alat")
                    print("4. Logout")
                    print("5. Keluar dari Program")

                    menu = int(input("Pilih menu: "))

                    if menu == 1:
                        nomor = int(input("Pilih nomor alat yang disewa: "))

                        if nomor > 0 and nomor <= len(alat):
                            indeks = nomor - 1

                            if alat[indeks][3] > 0:
                                nama_penyewa = input("Masukkan nama penyewa: ")
                                kontak = input("Masukkan nomor HP: ")
                                jumlah = int(input("Masukkan jumlah alat: "))
                                hari = int(input("Masukkan lama sewa (hari): "))

                                if jumlah > 0 and jumlah <= alat[indeks][3] and hari > 0:
                                    total = alat[indeks][2] * jumlah * hari

                                    print("\n========== KONFIRMASI SEWA ==========")
                                    print("Nama penyewa:", nama_penyewa)
                                    print("Nama alat:", alat[indeks][0])
                                    print("Jumlah:", jumlah)
                                    print("Lama sewa:", hari, "hari")
                                    print("Total harga: Rp.", total)

                                    konfirmasi = input("Lanjutkan? (y/n): ")

                                    if konfirmasi == "y" or konfirmasi == "Y":
                                        penyewaan.append([
                                            nama_penyewa,
                                            kontak,
                                            alat[indeks][0],
                                            jumlah,
                                            hari,
                                            total,
                                            "Disewa",
                                            username
                                        ])

                                        alat[indeks][3] -= jumlah

                                        print("Penyewaan berhasil")
                                        print("Sisa stok:", alat[indeks][3])
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

                        for i in range(len(penyewaan)):
                            if penyewaan[i][7] == username:
                                ada_pesanan = True

                                print(
                                    i + 1, "|",
                                    penyewaan[i][0], "|",
                                    penyewaan[i][2], "|",
                                    "Jumlah:", penyewaan[i][3], "|",
                                    "Hari:", penyewaan[i][4], "|",
                                    "Total: Rp.", penyewaan[i][5], "|",
                                    "Status:", penyewaan[i][6]
                                )

                        if ada_pesanan == False:
                            print("Belum ada penyewaan")

                    elif menu == 3:
                        ada_pesanan = False

                        for i in range(len(penyewaan)):
                            if (
                                penyewaan[i][7] == username
                                and penyewaan[i][6] == "Disewa"
                            ):
                                ada_pesanan = True
                                print(
                                    i + 1, "|",
                                    penyewaan[i][2], "|",
                                    "Jumlah:", penyewaan[i][3]
                                )

                        if ada_pesanan == True:
                            nomor = int(input("Nomor penyewaan yang dikembalikan: "))

                            if nomor > 0 and nomor <= len(penyewaan):
                                indeks = nomor - 1

                                if penyewaan[indeks][7] == username:
                                    if penyewaan[indeks][6] == "Disewa":
                                        for i in range(len(alat)):
                                            if alat[i][0] == penyewaan[indeks][2]:
                                                alat[i][3] += penyewaan[indeks][3]
                                                break

                                        penyewaan[indeks][6] = "Dikembalikan"
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
        username_ada = False

        for i in range(len(user)):
            if nama_baru == user[i][0]:
                username_ada = True

        if nama_baru == "":
            print("Username tidak boleh kosong")
        elif username_ada == True:
            print("Username sudah digunakan")
        else:
            password_baru = input("Masukkan password baru: ")

            if password_baru == "":
                print("Password tidak boleh kosong")
            else:
                user.append([
                    nama_baru,
                    password_baru,
                    "pengguna"
                ])

                print("Registrasi berhasil")
                print("Silakan login menggunakan akun baru")

        input("\nTekan Enter untuk kembali ke menu utama.")

    elif menu_awal == 3:
        program_status = False
        os.system("cls")
        print("Program selesai. Terima kasih!")
    else:
        print("Menu tidak valid")