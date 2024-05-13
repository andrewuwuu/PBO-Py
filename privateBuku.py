class Buku:
    def __init__(self, judul_buku, pengarang):
        self._judul_buku = judul_buku
        self._pengarang = pengarang
        
    def info(self):
        print(f"Buku: {self._judul_buku} ({self._pengarang})")
        
buku1 = Buku("Feeling and Trembling", "Kierkegaard")
print(buku1._judul_buku)
buku1.info()