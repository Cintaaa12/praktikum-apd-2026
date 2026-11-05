from datetime import datetime

import data
from alat import cari_nama_alat
from fungsi import (buat_tabel, format_rupiah, input_angka, input_nomor_hp,
                   input_teks, pesan_error, pesan_sukses, pesan_info)


def hitung_total(harga, jumlah, hari):
    return harga * jumlah * hari


def ambil_nomor_penyewaan():
    nomor = data.nomor_penyewaan_baru
    data.nomor_penyewaan_baru += 1
    return nomor


def tampilkan_penyewaan(filter_username):
    tabel = buat_tabel("DAFTAR PENYEWAAN",
                       ["No", "Penyewa", "Kontak", "Alat", "Jumlah", "Hari",
                        "Total", "Tanggal Sewa", "Status"])
    ada_data = False

    for nomor in data.penyewaan:
        item = data.penyewaan[nomor]
        if filter_username == "" or item["username"] == filter_username:
            ada_data = True
            tabel.add_row([
                nomor,
                item["nama_penyewa"],
                item["kontak"],
                item["nama_alat"],
                item["jumlah"],
                item["hari"],
                format_rupiah(item["total"]),
                item["tanggal"],
                item["status"]
            ])

    if ada_data == False:
        pesan_info("Belum ada penyewaan")
    else:
        print()
        print(tabel)

    return ada_data


def sewa_alat(username):
    nomor_alat = input_angka("Pilih nomor alat yang disewa: ")
    nama_terpilih = cari_nama_alat(nomor_alat)

    if nama_terpilih == "":
        pesan_error("Nomor alat tidak valid")
        return

    if data.alat[nama_terpilih]["stok"] <= 0:
        pesan_error("Stok alat habis")
        return

    nama_penyewa = input_teks("Masukkan nama penyewa: ")
    kontak = input_nomor_hp()
    jumlah = input_angka("Masukkan jumlah alat: ")
    hari = input_angka("Masukkan lama sewa (hari): ")

    if jumlah <= 0 or jumlah > data.alat[nama_terpilih]["stok"] or hari <= 0:
        pesan_error("Jumlah atau lama sewa tidak valid")
        return

    total = hitung_total(data.alat[nama_terpilih]["harga"], jumlah, hari)

    tabel = buat_tabel("KONFIRMASI SEWA", ["Keterangan", "Isi"])
    tabel.add_row(["Nama penyewa", nama_penyewa])
    tabel.add_row(["Nama alat", nama_terpilih])
    tabel.add_row(["Jumlah", jumlah])
    tabel.add_row(["Lama sewa", str(hari) + " hari"])
    tabel.add_row(["Total harga", format_rupiah(total)])
    print()
    print(tabel)

    konfirmasi = input("Lanjutkan? (y/n): ")

    if konfirmasi == "y" or konfirmasi == "Y":
        nomor = ambil_nomor_penyewaan()
        data.penyewaan[nomor] = {
            "nama_penyewa": nama_penyewa,
            "kontak": kontak,
            "nama_alat": nama_terpilih,
            "jumlah": jumlah,
            "hari": hari,
            "total": total,
            "tanggal": datetime.now().strftime("%d-%m-%Y"),
            "status": "Disewa",
            "username": username
        }

        data.alat[nama_terpilih]["stok"] -= jumlah
        pesan_sukses("Penyewaan berhasil")
        print("Sisa stok:", data.alat[nama_terpilih]["stok"])
    else:
        pesan_info("Penyewaan dibatalkan")


def proses_pengembalian(username, role):
    tabel = buat_tabel("DAFTAR YANG BELUM DIKEMBALIKAN",
                       ["No", "Penyewa", "Alat", "Jumlah"])
    ada_pesanan = False

    for nomor in data.penyewaan:
        item = data.penyewaan[nomor]
        if item["status"] == "Disewa" and (role == "admin" or item["username"] == username):
            ada_pesanan = True
            tabel.add_row([nomor, item["nama_penyewa"], item["nama_alat"], item["jumlah"]])

    if ada_pesanan == False:
        pesan_info("Tidak ada alat yang perlu dikembalikan")
        return

    print()
    print(tabel)
    nomor = input_angka("Nomor penyewaan yang dikembalikan: ")

    try:
        item = data.penyewaan[nomor]

        if role != "admin" and item["username"] != username:
            pesan_error("Penyewaan tersebut bukan milik kamu")
        elif item["status"] != "Disewa":
            pesan_error("Alat sudah dikembalikan")
        else:
            data.alat[item["nama_alat"]]["stok"] += item["jumlah"]
            item["status"] = "Dikembalikan"
            pesan_sukses("Pengembalian berhasil")
    except KeyError:
        pesan_error("Nomor penyewaan tidak valid atau data alat sudah dihapus")
