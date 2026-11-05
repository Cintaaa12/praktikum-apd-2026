import data
from fungsi import (buat_tabel, format_rupiah, input_angka, input_teks,
                   pesan_error, pesan_sukses)


def tampilkan_daftar_alat():
    tabel = buat_tabel("DAFTAR ALAT",
                       ["No", "Nama Alat", "Kategori", "Harga/Hari", "Stok"])
    i = 1
    for nama_alat in data.alat:
        tabel.add_row([
            i,
            nama_alat,
            data.alat[nama_alat]["kategori"],
            format_rupiah(data.alat[nama_alat]["harga"]),
            data.alat[nama_alat]["stok"]
        ])
        i += 1
    print()
    print(tabel)


def cari_nama_alat(nomor_alat):
    nama_terpilih = ""
    i = 1

    for nama_alat in data.alat:
        if i == nomor_alat:
            nama_terpilih = nama_alat
        i += 1

    return nama_terpilih


def cek_sedang_disewa(nama_alat):
    for nomor in data.penyewaan:
        if data.penyewaan[nomor]["nama_alat"] == nama_alat and data.penyewaan[nomor]["status"] == "Disewa":
            return True
    return False


def hitung_stok_rekursif(daftar_nama, indeks):
    if indeks == len(daftar_nama):
        return 0
    stok_sekarang = data.alat[daftar_nama[indeks]]["stok"]
    return stok_sekarang + hitung_stok_rekursif(daftar_nama, indeks + 1)


def tambah_alat():
    nama_alat = input_teks("Masukkan nama alat: ")

    if nama_alat in data.alat:
        pesan_error("Nama alat sudah tersedia")
        return

    kategori = input_teks("Masukkan kategori alat: ")
    harga = input_angka("Masukkan harga sewa per hari: ")
    stok = input_angka("Masukkan jumlah stok: ")

    if harga <= 0 or stok < 0:
        pesan_error("Harga harus lebih dari 0 dan stok tidak boleh negatif")
        return

    data.alat[nama_alat] = {
        "kategori": kategori,
        "harga": harga,
        "stok": stok
    }
    pesan_sukses("Alat berhasil ditambahkan")


def hapus_alat():
    tabel = buat_tabel("HAPUS ALAT", ["No", "Nama Alat", "Kategori"])
    i = 1
    for nama_alat in data.alat:
        tabel.add_row([i, nama_alat, data.alat[nama_alat]["kategori"]])
        i += 1
    print()
    print(tabel)

    nomor_alat = input_angka("Nomor alat yang ingin dihapus: ")
    nama_terpilih = cari_nama_alat(nomor_alat)

    if nama_terpilih == "":
        pesan_error("Nomor alat tidak valid")
    elif cek_sedang_disewa(nama_terpilih) == True:
        pesan_error("Alat masih disewa dan belum dikembalikan")
    else:
        tabel_alasan = buat_tabel("ALASAN PENGHAPUSAN", ["No", "Alasan"])
        tabel_alasan.add_row([1, "Rusak"])
        tabel_alasan.add_row([2, "Hilang"])
        print(tabel_alasan)
        alasan = input_angka("Pilih alasan penghapusan: ")

        if alasan == 1 or alasan == 2:
            try:
                del data.alat[nama_terpilih]
                pesan_sukses("Data alat berhasil dihapus")
            except KeyError:
                pesan_error("Data alat tidak ditemukan")
        else:
            pesan_error("Pilihan tidak valid")
