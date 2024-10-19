# Kelas dasar Musik
class Musik:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def tampilkan(self):
        return f"{self.judul:<20} {self.penyanyi:<20} {self.genre:<10}"

# Kelas turunan untuk menambah musik
class TambahMusik(Musik):
    daftar_musik = []

    def __init__(self, judul, penyanyi, genre):
        super().__init__(judul, penyanyi, genre)

    def tambah_musik(self):
        self.daftar_musik.append(self)

# Kelas untuk menampilkan musik berdasarkan genre
class TampilkanSemuaMusik:
    @staticmethod
    def tampilkan_semua_japanese():
        print(f"{'Judul':<20} {'Penyanyi':<20} {'Genre':<10}")
        print("=" * 50)
        for musik in TambahMusik.daftar_musik:
            if musik.genre == "J-Song":
                print(musik.tampilkan())

    @staticmethod
    def tampilkan_semua_korean():
        print(f"{'Judul':<20} {'Penyanyi':<20} {'Genre':<10}")
        print("=" * 50)
        for musik in TambahMusik.daftar_musik:
            if musik.genre == "K-Song":
                print(musik.tampilkan())

    @staticmethod
    def tampilkan_semua_english():
        print(f"{'Judul':<20} {'Penyanyi':<20} {'Genre':<10}")
        print("=" * 50)
        for musik in TambahMusik.daftar_musik:
            if musik.genre == "E-Song":
                print(musik.tampilkan())

    @staticmethod
    def tampilkan_semua():
        if TambahMusik.daftar_musik:
            print(f"{'Judul':<20} {'Penyanyi':<20} {'Genre':<10}")
            print("=" * 50)
            for musik in TambahMusik.daftar_musik:
                print(musik.tampilkan())
        else:
            print("Tidak ada musik dalam daftar.")

# Kelas untuk mencari musik berdasarkan penyanyi
class CariMusik:
    @staticmethod
    def cari_berdasarkan_penyanyi(penyanyi):
        ditemukan = False
        print(f"{'Judul':<20} {'Penyanyi':<20} {'Genre':<10}")
        print("=" * 50)
        for musik in TambahMusik.daftar_musik:
            if musik.penyanyi.lower() == penyanyi.lower():
                print(musik.tampilkan())
                ditemukan = True
        if not ditemukan:
            print(f"Tidak ada musik ditemukan dari penyanyi '{penyanyi}'.")

# Kelas untuk menghapus musik
class HapusMusik:
    @staticmethod
    def hapus_judul(judul):
        for musik in TambahMusik.daftar_musik:
            if musik.judul.lower() == judul.lower():
                TambahMusik.daftar_musik.remove(musik)
                print(f"Musik '{judul}' telah dihapus.")
                return
        print(f"Musik '{judul}' tidak ditemukan.")

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n========== Playlist Music ==========")
    print("1. Tampilkan Japanese Songs")
    print("2. Tampilkan Korean Songs")
    print("3. Tampilkan English Songs")
    print("4. Tampilkan Semua Musik")
    print("5. Cari Musik berdasarkan Penyanyi")
    print("0. Keluar")

# Fungsi untuk menambah musik
def tambah_musik(genre):
    judul = input("Masukkan judul musik: ")
    penyanyi = input("Masukkan nama penyanyi: ")
    TambahMusik(judul, penyanyi, genre).tambah_musik()
    print(f"Musik '{judul}' oleh {penyanyi} telah ditambahkan ke {genre}.")

# Fungsi utama
def main():
    # Menambahkan beberapa musik contoh
    # Japanese Songs
    TambahMusik("Sparkle", "Radwimps", "J-Song").tambah_musik()
    TambahMusik("Suzume", "Radwimps", "J-Song").tambah_musik()
    TambahMusik("Lemon", "Kenshi Yonezu", "J-Song").tambah_musik()
    TambahMusik("Koi wa Sensou", "Aimer", "J-Song").tambah_musik()
    TambahMusik("Zenzenzense", "Radwimps", "J-Song").tambah_musik()

    # Korean Songs
    TambahMusik("Gangnam Style", "PSY", "K-Song").tambah_musik()
    TambahMusik("Dynamite", "BTS", "K-Song").tambah_musik()
    TambahMusik("Love Scenario", "iKON", "K-Song").tambah_musik()
    TambahMusik("Lovesick Girls", "BLACKPINK", "K-Song").tambah_musik()
    TambahMusik("Cheer Up", "TWICE", "K-Song").tambah_musik()

    # English Songs
    TambahMusik("Shape of You", "Ed Sheeran", "E-Song").tambah_musik()
    TambahMusik("Blinding Lights", "The Weeknd", "E-Song").tambah_musik()
    TambahMusik("Someone You Loved", "Lewis Capaldi", "E-Song").tambah_musik()
    TambahMusik("Bad Guy", "Billie Eilish", "E-Song").tambah_musik()
    TambahMusik("Rolling in the Deep", "Adele", "E-Song").tambah_musik()

    while True:
        tampilkan_menu()
        pilihan = input("\nMasukkan Pilihan Menu: ")

        if pilihan == '0':
            print("Keluar dari program.")
            break
        elif pilihan == '1':
            print("\n>> Menampilkan Japanese Songs")
            TampilkanSemuaMusik.tampilkan_semua_japanese()
            if input("Ingin menambah musik? (y/n): ").lower() == 'y':
                tambah_musik("J-Song")
            if input("Ingin menghapus musik? (y/n): ").lower() == 'y':
                judul_hapus = input("Masukkan judul musik yang ingin dihapus: ")
                HapusMusik.hapus_judul(judul_hapus)
                print("\n>> Menampilkan Japanese Songs Setelah Penghapusan")
                TampilkanSemuaMusik.tampilkan_semua_japanese()
        elif pilihan == '2':
            print("\n>> Menampilkan Korean Songs")
            TampilkanSemuaMusik.tampilkan_semua_korean()
            if input("Ingin menambah musik? (y/n): ").lower() == 'y':
                tambah_musik("K-Song")
            if input("Ingin menghapus musik? (y/n): ").lower() == 'y':
                judul_hapus = input("Masukkan judul musik yang ingin dihapus: ")
                HapusMusik.hapus_judul(judul_hapus)
                print("\n>> Menampilkan Korean Songs Setelah Penghapusan")
                TampilkanSemuaMusik.tampilkan_semua_korean()
        elif pilihan == '3':
            print("\n>> Menampilkan English Songs")
            TampilkanSemuaMusik.tampilkan_semua_english()
            if input("Ingin menambah musik? (y/n): ").lower() == 'y':
                tambah_musik("E-Song")
            if input("Ingin menghapus musik? (y/n): ").lower() == 'y':
                judul_hapus = input("Masukkan judul musik yang ingin dihapus: ")
                HapusMusik.hapus_judul(judul_hapus)
                print("\n>> Menampilkan English Songs Setelah Penghapusan")
                TampilkanSemuaMusik.tampilkan_semua_english()
        elif pilihan == '4':
            print("\n>> Menampilkan Semua Musik")
            TampilkanSemuaMusik.tampilkan_semua()
            judul_hapus = input("Masukkan judul musik yang ingin dihapus: ")
            HapusMusik.hapus_judul(judul_hapus)
        elif pilihan == '5':
            print("\n>> Cari Musik")
            penyanyi = input("Masukkan Penyanyi yang Ingin Dicari: ")
            CariMusik.cari_berdasarkan_penyanyi(penyanyi)
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Memulai program
if __name__ == "__main__":  
    main()




