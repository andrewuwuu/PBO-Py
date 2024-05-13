class Buku:
    def __init__(self, judul_buku, pengarang):
        self._judul_buku = judul_buku
        self._pengarang = pengarang
        
    def info(self):
        print(f"Buku: {self._judul_buku} ({self._pengarang})")
        
class bukuFiksi(Buku):
    def __init__(self, judul_buku, pengarang, tahun):
        super().__init__(judul_buku, pengarang)
        self.__tahun = tahun
        
    def info(self):
        super().info()
        print(f"Tahun terbit: {self.__tahun} ")
        
bukuFiksi1 = bukuFiksi("O", "Eka Kurniawan", 2016)
#print(bukuFiksi.__judul_buku) -- Error 'bukuFiksi' object has no attribute '__judul_buku'
bukuFiksi1.info()