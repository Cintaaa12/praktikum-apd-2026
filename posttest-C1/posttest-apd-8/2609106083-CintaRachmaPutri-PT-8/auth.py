import data
from fungsi import judul, pesan_error, pesan_sukses, pesan_info


def proses_login(sisa_kesempatan):
    if sisa_kesempatan == 0:
        return ""

    judul("\n========== LOGIN ==========")
    nama = input("Masukkan username: ")
    password = input("Masukkan password: ")

    try:
        if password == data.user[nama]["password"]:
            return nama
        pesan_error("Username atau password salah")
    except KeyError:
        pesan_error("Username atau password salah")

    if sisa_kesempatan - 1 > 0:
        pesan_info("Login tersisa: " + str(sisa_kesempatan - 1) + " kali")

    return proses_login(sisa_kesempatan - 1)


def register():
    judul("========== REGISTER ==========")

    nama_baru = input("Masukkan username baru: ").strip()

    if nama_baru == "":
        pesan_error("Username tidak boleh kosong")
    elif nama_baru in data.user:
        pesan_error("Username sudah digunakan")
    else:
        password_baru = input("Masukkan password baru: ")

        if password_baru == "":
            pesan_error("Password tidak boleh kosong")
        else:
            data.user[nama_baru] = {
                "password": password_baru,
                "role": "pengguna"
            }
            pesan_sukses("Registrasi berhasil")
            pesan_info("Silakan login menggunakan akun baru")
