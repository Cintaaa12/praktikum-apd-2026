import os
from colorama import init, Fore, Style
from prettytable import PrettyTable

init(autoreset=True)


def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pesan_sukses(teks):
    print(Fore.GREEN + teks)


def pesan_error(teks):
    print(Fore.RED + teks)


def pesan_info(teks):
    print(Fore.YELLOW + teks)


def judul(teks):
    print(Fore.CYAN + Style.BRIGHT + teks)


def format_rupiah(angka):
    return "Rp. " + f"{angka:,}".replace(",", ".")


def buat_tabel(judul_tabel, kolom):
    tabel = PrettyTable()
    tabel.title = judul_tabel
    tabel.field_names = kolom
    tabel.align = "l"
    return tabel


def tampilkan_menu(judul_menu, daftar_menu):
    tabel = buat_tabel(judul_menu, ["No", "Menu"])
    nomor = 1
    for isi in daftar_menu:
        tabel.add_row([nomor, isi])
        nomor += 1
    print()
    print(tabel)


def input_angka(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            return nilai
        except ValueError:
            pesan_error("Error: input harus berupa angka bulat")


def input_teks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            pesan_error("Error: input tidak boleh kosong")
        else:
            return teks


def input_nomor_hp():
    while True:
        try:
            kontak = input("Masukkan nomor HP: ")
            if kontak.isdigit() == False:
                raise ValueError("Nomor HP hanya boleh berisi angka")
            if len(kontak) < 10 or len(kontak) > 13:
                raise ValueError("Nomor HP harus 10 sampai 13 digit")
            return kontak
        except ValueError as pesan:
            pesan_error("Error: " + str(pesan))


def tekan_enter(pesan):
    input("\n" + pesan)
