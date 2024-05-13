class Buku:
    def __init__(self, jenis_buku, judul_buku, pengarang):
        self.jenis_buku = jenis_buku
        self.judul_buku = judul_buku
        self.pengarang = pengarang

    def info(self):
        print(f"Jenis Buku: {self.jenis_buku}")
        print(f"Judul Buku: {self.judul_buku}")
        print(f"Pengarang : {self.pengarang}")

buku1 = Buku("Fiksi", "Orang Asing", "Albert Camus")
buku1.info()