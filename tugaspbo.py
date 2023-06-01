# Kelas-kelas ini mewakili seorang mahasiswa, sebuah jurusan, dan sebuah universitas, secara berturut-turut.
# Kelas Mahasiswa mewakili seorang mahasiswa dan memiliki atribut seperti nama, NIM, dan jurusan yang diikuti mahasiswa tersebut.
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

# Kelas ini memiliki metode 'tampilkan_info' yang menampilkan informasi lengkap mahasiswa.
    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)

# Kelas sebuah jurusan dan memiliki atribut nama jurusan serta daftar menyimpan mahasiswa-mahasiswa dalam jurusan tersebut.
class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

# Kelas menambahkan mahasiswa ke jurusan 
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

# dan menampilkan daftar mahasiswa dalam jurusan.
    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama:", mahasiswa.nama)
            print("NIM:", mahasiswa.nim)
            print()

# Kelas Universitas mewakili universitas dan memiliki  nama universitas serta sebuah daftar untuk menyimpan jurusan-jurusan dalam universitas tersebut.
class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

# Kelas ini adalah metode untuk menambahkan jurusan ke universitas 
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

# menampilkan daftar jurusan dalam universitas tersebut.
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)

# Membuat objek Universitas dengan nama "Bengkulu University"
universitas_bengkulu = Universitas("Bengkulu")

# Membuat objek dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas Bengkulu
jurusan_ti = Jurusan("Teknik Informatika")
universitas_bengkulu.tambah_jurusan(jurusan_ti)

# Membuat objek dengan nama "Lola Yashinta Dewi", NIM "G1A022009",
#    dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas Bengkulu
mahasiswa_lola = Mahasiswa("Lola Yashinta Dewi", "G1A022009", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa_lola)

# Menampilkan daftar jurusan yang ada di Universitas Bengkulu
universitas_bengkulu.tampilkan_daftar_jurusan()

# Menampilkan  mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas Bengkulu
jurusan_ti.tampilkan_daftar_mahasiswa()
