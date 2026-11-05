import data
from alat import (hapus_alat, hitung_stok_rekursif, tambah_alat,
                  tampilkan_daftar_alat)
from auth import proses_login
from penyewaan import proses_pengembalian, sewa_alat, tampilkan_penyewaan
from fungsi import (bersihkan_layar, input_angka, pesan_error, pesan_info,
                   pesan_sukses, tampilkan_menu, tekan_enter)


def menu_admin():
    logout = False

    while data.program_status == True and logout == False:
        tampilkan_daftar_alat()
        tampilkan_menu("MENU ADMIN", [
            "Tambah Alat",
            "Lihat Semua Penyewaan",
            "Update Pengembalian",
            "Hapus Alat Rusak/Hilang",
            "Lihat Total Stok",
            "Logout",
            "Keluar dari Program"
        ])

        menu = input_angka("Pilih menu: ")

        if menu == 1:
            tambah_alat()
        elif menu == 2:
            tampilkan_penyewaan("")
        elif menu == 3:
            proses_pengembalian("admin", "admin")
        elif menu == 4:
            hapus_alat()
        elif menu == 5:
            total_stok = hitung_stok_rekursif(list(data.alat.keys()), 0)
            pesan_info("Total seluruh stok alat: " + str(total_stok))
        elif menu == 6:
            logout = True
            bersihkan_layar()
            pesan_sukses("Logout berhasil")
        elif menu == 7:
            data.program_status = False
            logout = True
            bersihkan_layar()
            pesan_info("Program selesai")
        else:
            pesan_error("Menu tidak valid")

        if logout == False and data.program_status == True:
            tekan_enter("Tekan Enter untuk melanjutkan.")
            bersihkan_layar()


def menu_pengguna(username):
    logout = False

    while data.program_status == True and logout == False:
        tampilkan_daftar_alat()
        tampilkan_menu("MENU PENGGUNA", [
            "Sewa Alat",
            "Lihat Penyewaan Saya",
            "Kembalikan Alat",
            "Logout",
            "Keluar dari Program"
        ])

        menu = input_angka("Pilih menu: ")

        if menu == 1:
            sewa_alat(username)
        elif menu == 2:
            tampilkan_penyewaan(username)
        elif menu == 3:
            proses_pengembalian(username, "pengguna")
        elif menu == 4:
            logout = True
            bersihkan_layar()
            pesan_sukses("Logout berhasil")
        elif menu == 5:
            data.program_status = False
            logout = True
            bersihkan_layar()
            pesan_info("Program selesai")
        else:
            pesan_error("Menu tidak valid")

        if logout == False and data.program_status == True:
            tekan_enter("Tekan Enter untuk melanjutkan.")
            bersihkan_layar()


def menu_login():
    username = proses_login(3)

    if username == "":
        pesan_error("\nKesempatan login habis")
        tekan_enter("Tekan Enter untuk kembali...")
        return

    role = data.user[username]["role"]
    pesan_sukses("\nLogin berhasil")
    print("Selamat datang", username)
    print("Role anda adalah", role)

    if role == "admin":
        menu_admin()
    else:
        menu_pengguna(username)
