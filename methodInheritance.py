class Buku:
    def __init__(self, jenis_buku, judul_buku, pengarang):
        self.jenis_buku = jenis_buku
        self.judul_buku = judul_buku
    
    def info(self):
        print(f"Buku: {self.jenis_buku} ({self.judul_buku})")
        
class bukuFiksi(Buku):
    def __init__(self, jenis_buku, judul_buku, pengarang, tahun):
        super().__init__(jenis_buku, judul_buku, pengarang)
        self.tahun = tahun
        
    def info(self):
        print(f"Mobil: {self.jenis_buku} ({self.judul_buku}) - Tahun Terbit: {self.tahun}")