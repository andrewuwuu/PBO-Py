class Buku:
    jenis_buku = ""
    judul_buku = ""
    pengarang = ""

    def membaca(self, judul_buku):
        print("Saya membaca buku berjudul " + judul_buku)
    
    def genre_buku(self, judul_buku, jenis_buku):
        print("Genre buku " + judul_buku + " adalah " + jenis_buku)
    
    def penulis(self, judul_buku, pengarang):
        print("Penulis dari buku " + judul_buku + " adalah " + pengarang)

buku1 = Buku()
buku1.jenis_buku = "Fiksi"
buku1.judul_buku = "Orang Asing"
buku1.pengarang = "Albert Camus"

buku1.membaca(buku1.judul_buku)
buku1.genre_buku(buku1.judul_buku, buku1.jenis_buku)
buku1.penulis(buku1.judul_buku, buku1.pengarang)

buku2 = Buku()
buku2.jenis_buku = "Fiksi"
buku2.judul_buku = "Cantik Itu Luka"
buku2.pengarang = "Eka Kurniawan"

buku2.membaca(buku2.judul_buku)
buku2.genre_buku(buku2.judul_buku, buku2.jenis_buku)
buku2.penulis(buku2.judul_buku, buku2.pengarang)