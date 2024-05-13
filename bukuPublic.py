class Buku:
    def __init__(self, judul_buku, pengarang):
        self.judul_buku = judul_buku
        self.pengarang = pengarang
        
    def info(self):
        print(f"Buku: {self.judul_buku} ({self.pengarang})")
        
buku1 = Buku("Feeling and Trembling", "Kierkegaard")
print(buku1.judul_buku)
buku1.info()