username_benar = "cinta"
password_benar = "083"
saldo_awal = 5000000
status = True

print("-------- Selamat datang di ATM ---------")
for i in range(1,4):
    username = input("Silahkan masukkan username Anda: ")
    password = input("Silahkan masukkan password Anda: ")
    if username == username_benar and password == password_benar:
        print("\n-------- Selamat Login berhasil! --------")
        while status == True:
            print("\n------ Menu ATM ------ ")
            print("1. Cek Saldo")
            print("2. Tarik Tunai")
            print("3. Setor Tunai")
            print("4. Keluar")
            pilihan = input("Silahkan pilih menu (1-4): ")
            if pilihan == "1":
                print(f"\nSaldo Anda saat ini adalah: Rp{saldo_awal}")
            elif pilihan == "2":
                nominal_tarik = int(input("\nMasukkan nominal yang ingin ditarik: Rp "))
                if nominal_tarik % 100000 != 0 or nominal_tarik <= 0:
                    print("\nNominal harus kelipatan Rp 100000")
                    continue
                elif nominal_tarik > saldo_awal:
                    print("\nMaaf, saldo Anda tidak mencukupi.")
                    print(f"Saldo Anda yang tersisa saat ini adalah: Rp{saldo_awal}")
                else:
                    saldo_awal -= nominal_tarik
                    print(f"\nTransaksi berhasil. Saldo Anda saat ini adalah: Rp{saldo_awal}")
            elif pilihan == "3":
                nominal_setor = int(input("\nMasukkan nominal yang ingin disetor: Rp "))
                if nominal_setor <= 0 or nominal_setor % 100000 != 0:
                    print("\nNominal harus kelipatan Rp 100000 dan harus lebih dari Rp 0.")
                    continue
                saldo_awal += nominal_setor
                print(f"\nSetoran Anda adalah: Rp{nominal_setor}")
                print(f"Penyetoran berhasil. Total Saldo Anda saat ini adalah: Rp{saldo_awal}")
            elif pilihan == "4":
                print("\nTerima kasih telah menggunakan ATM ini.")
                status = False
                break
        break
    else:
        sisa_percobaan = 3 - i
        if sisa_percobaan > 0:
            print(f"\nLogin Gagal! Sisa percobaan Anda: {sisa_percobaan}x percobaan lagi.")
        else:
            print("\nAnda telah gagal login sebanyak 3 kali. Akun Anda telah diblokir.")