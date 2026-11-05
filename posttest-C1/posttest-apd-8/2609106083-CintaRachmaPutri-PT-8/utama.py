import data
from auth import register
from menu import menu_login
from fungsi import (bersihkan_layar, input_angka, pesan_error, pesan_info,
                   pesan_sukses, tampilkan_menu, tekan_enter)


def main():
    while data.program_status == True:
        bersihkan_layar()

        tampilkan_menu("SISTEM PERSEWAAN ALAT OUTDOOR/CAMPING", [
            "Login",
            "Register",
            "Keluar dari Program"
        ])

        menu_awal = input_angka("Pilih menu: ")

        if menu_awal == 1:
            menu_login()
        elif menu_awal == 2:
            bersihkan_layar()
            register()
            tekan_enter("Tekan Enter untuk kembali ke menu utama.")
        elif menu_awal == 3:
            data.program_status = False
            bersihkan_layar()
            pesan_sukses("Program selesai. Terima kasih!")
        else:
            pesan_error("Menu tidak valid")
            tekan_enter("Tekan Enter untuk melanjutkan.")


main() 

