import math
from datetime import datetime

# ==============================
# DATA AKUN
# ==============================

akun = {
    "paijaa": {
        "password": "tupai123",
        "role": "admin"
    },
    "noni": {
        "password": "belanda123",
        "role": "user"
    }
}

data_atlet = []


# ==============================
# FUNCTION LOGIN
# ==============================

def login():
    print("\n========================================")
    print("          LOGIN SISTEM JUDO")
    print("========================================")

    kesempatan = 3

    while kesempatan > 0:
        username = input("Username : ")
        password = input("Password : ")

        if username in akun and akun[username]["password"] == password:
            print("\nLogin berhasil!")
            print("Selamat datang,", username)
            print("Role :", akun[username]["role"])

            return akun[username]["role"]

        else:
            kesempatan -= 1
            print("\nUsername atau password salah.")
            print("Sisa percobaan:", kesempatan)

    print("\nPercobaan login habis.")
    return None


# ==============================
# FUNCTION INPUT UMUR
# ==============================

def input_umur():
    while True:
        umur = input("Umur             : ")

        angka = True

        if umur == "":
            angka = False
        else:
            for karakter in umur:
                if karakter < "0" or karakter > "9":
                    angka = False
                    break

        if angka:
            umur = int(umur)

            if umur > 0 and math.isfinite(umur):
                return umur
            else:
                print("Umur harus lebih dari 0.")
        else:
            print("Umur harus berupa angka.")


# ==============================
# FUNCTION INPUT BERAT
# ==============================

def input_berat():
    while True:
        berat = input("Berat Badan (kg) : ")

        angka = True
        titik = 0

        if berat == "":
            angka = False
        else:
            for karakter in berat:
                if karakter == ".":
                    titik += 1

                    if titik > 1:
                        angka = False
                        break

                elif karakter < "0" or karakter > "9":
                    angka = False
                    break

        if angka and berat != ".":
            berat = float(berat)

            if berat > 0 and math.isfinite(berat):
                return berat
            else:
                print("Berat badan harus lebih dari 0 kg.")
        else:
            print("Berat badan harus berupa angka.")


# ==============================
# FUNCTION TAMPILKAN DATA
# ==============================

def tampilkan_data():
    print("\n================================ DATA ATLET JUDO ================================")

    if len(data_atlet) == 0:
        print("Belum ada data atlet.")

    else:
        for i, atlet in enumerate(data_atlet, start=1):
            print("\nAtlet ke-", i)
            print("Nama               :", atlet["nama"])
            print("Umur               :", atlet["umur"], "tahun")
            print("Jenis Kelamin      :", atlet["jenis_kelamin"])
            print("Berat Badan        :", atlet["berat"], "kg")
            print("Kelas Pertandingan :", atlet["kelas"])
            print("Asal Klub          :", atlet["klub"])
            print("Tanggal Input      :", atlet["tanggal"])

    print("=================================================================================")


# ==============================
# FUNCTION TAMBAH DATA
# ==============================

def tambah_data():
    print("\n========== TAMBAH DATA ATLET ==========")

    while True:
        nama = input("Nama             : ").strip()

        if nama != "":
            break
        else:
            print("Nama tidak boleh kosong.")

    umur = input_umur()

    while True:
        jenis_kelamin = input("Jenis Kelamin (L/P): ").upper()

        if jenis_kelamin == "L" or jenis_kelamin == "P":
            break
        else:
            print("Jenis kelamin hanya boleh L atau P.")

    berat = input_berat()

    while True:
        kelas = input("Kelas Pertandingan: ").strip()

        if kelas != "":
            break
        else:
            print("Kelas pertandingan tidak boleh kosong.")

    while True:
        klub = input("Asal Klub        : ").strip()

        if klub != "":
            break
        else:
            print("Asal klub tidak boleh kosong.")

    atlet_baru = {
        "nama": nama,
        "umur": umur,
        "jenis_kelamin": jenis_kelamin,
        "berat": berat,
        "kelas": kelas,
        "klub": klub,
        "tanggal": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    data_atlet.append(atlet_baru)

    print("\nData atlet berhasil ditambahkan!")


# ==============================
# FUNCTION UBAH DATA
# ==============================

def ubah_data():
    print("\n========== UBAH DATA ATLET ==========")

    if len(data_atlet) == 0:
        print("Belum ada data atlet.")
        return

    tampilkan_data()

    while True:
        nomor = input("Pilih nomor atlet yang ingin diubah: ")

        angka = True

        if nomor == "":
            angka = False
        else:
            for karakter in nomor:
                if karakter < "0" or karakter > "9":
                    angka = False
                    break

        if angka:
            nomor = int(nomor)

            if 1 <= nomor <= len(data_atlet):
                break
            else:
                print("Nomor atlet tidak tersedia.")
        else:
            print("Input harus berupa angka.")

    index = nomor - 1

    print("\nMasukkan data baru:")

    while True:
        nama = input("Nama             : ").strip()

        if nama != "":
            break
        else:
            print("Nama tidak boleh kosong.")

    umur = input_umur()

    while True:
        jenis_kelamin = input("Jenis Kelamin (L/P): ").upper()

        if jenis_kelamin == "L" or jenis_kelamin == "P":
            break
        else:
            print("Jenis kelamin hanya boleh L atau P.")

    berat = input_berat()

    while True:
        kelas = input("Kelas Pertandingan: ").strip()

        if kelas != "":
            break
        else:
            print("Kelas pertandingan tidak boleh kosong.")

    while True:
        klub = input("Asal Klub        : ").strip()

        if klub != "":
            break
        else:
            print("Asal klub tidak boleh kosong.")

    data_atlet[index] = {
        "nama": nama,
        "umur": umur,
        "jenis_kelamin": jenis_kelamin,
        "berat": berat,
        "kelas": kelas,
        "klub": klub,
        "tanggal": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    print("\nData atlet berhasil diubah!")


# ==============================
# FUNCTION HAPUS DATA
# ==============================

def hapus_data():
    print("\n========== HAPUS DATA ATLET ==========")

    if len(data_atlet) == 0:
        print("Belum ada data atlet.")
        return

    tampilkan_data()

    while True:
        nomor = input("Pilih nomor atlet yang ingin dihapus: ")

        angka = True

        if nomor == "":
            angka = False
        else:
            for karakter in nomor:
                if karakter < "0" or karakter > "9":
                    angka = False
                    break

        if angka:
            nomor = int(nomor)

            if 1 <= nomor <= len(data_atlet):
                break
            else:
                print("Nomor atlet tidak tersedia.")
        else:
            print("Input harus berupa angka.")

    index = nomor - 1

    print("\nData yang akan dihapus:", data_atlet[index]["nama"])

    while True:
        konfirmasi = input("Yakin ingin menghapus? (Y/N): ").upper()

        if konfirmasi == "Y":
            data_atlet.pop(index)
            print("Data atlet berhasil dihapus!")
            break

        elif konfirmasi == "N":
            print("Penghapusan dibatalkan.")
            break

        else:
            print("Masukkan Y atau N.")


# ==============================
# MENU ADMIN
# ==============================

def menu_admin():
    while True:
        print("\n========================================")
        print("       SISTEM PENDATAAN ATLET JUDO")
        print("              ROLE: ADMIN")
        print("========================================")
        print("1. Tambah Data Atlet")
        print("2. Lihat Seluruh Data")
        print("3. Ubah Data Atlet")
        print("4. Hapus Data Atlet")
        print("5. Logout")
        print("========================================")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            tampilkan_data()

        elif pilihan == "3":
            ubah_data()

        elif pilihan == "4":
            hapus_data()

        elif pilihan == "5":
            print("\nLogout berhasil.")
            break

        else:
            print("Pilihan tidak tersedia.")


# ==============================
# MENU USER
# ==============================

def menu_user():
    while True:
        print("\n========================================")
        print("       SISTEM PENDATAAN ATLET JUDO")
        print("               ROLE: USER")
        print("========================================")
        print("1. Lihat Data Atlet")
        print("2. Logout")
        print("========================================")

        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            tampilkan_data()

        elif pilihan == "2":
            print("\nLogout berhasil.")
            break

        else:
            print("Pilihan tidak tersedia.")


# ==============================
# PROGRAM UTAMA
# ==============================

while True:

    role = login()

    if role == "admin":
        menu_admin()

    elif role == "user":
        menu_user()

    else:
        print("\nProgram selesai.")
        break