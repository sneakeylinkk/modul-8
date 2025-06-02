def data_awal():
    inventaris = {
        "9781234567897": {
            "Judul": "Matematika Peminatan",
            "Penulis": "Hezvin",
            "Stok": 10,
            "Harga Beli": 50000,
            "Harga Jual": 75000},
        "9781234567898": {
            "Judul": "Matematika Umum",
            "Penulis": "Ariqah",
            "Stok": 4,
            "Harga Beli": 60000,
            "Harga Jual": 100000},
        "9781234567899": {
            "Judul": "Fisika",
            "Penulis": "Dwiana",
            "Stok": 3,
            "Harga Beli": 70000,
            "Harga Jual": 110000},
        "9781234567800": {
            "Judul": "Kimia",
            "Penulis": "Pujhi",
            "Stok": 8,
            "Harga Beli": 45000,
            "Harga Jual": 70000},
        "9781234567801": {
            "Judul": "Biologi",
            "Penulis": "Nayla",
            "Stok": 6,
            "Harga Beli": 55000,
            "Harga Jual": 80000},
        "9781234567802": {
            "Judul": "Ilmu Pengetahuan Alam",
            "Penulis": "Mutiara",
            "Stok": 2,
            "Harga Beli": 95000,
            "Harga Jual": 120000},
        "9781234567803": {
            "Judul": "Ilmu Pengetahuan Sosial",
            "Penulis": "Khanaya",
            "Stok": 7,
            "Harga Beli": 48000,
            "Harga Jual": 75000},
        "9781234567804": {
            "Judul": "Kewarganegaraan",
            "Penulis": "Marcella",
            "Stok": 9,
            "Harga Beli": 52000,
            "Harga Jual": 78000},
        "9781234567805": {
            "Judul": "Agama",
            "Penulis": "Chelsea",
            "Stok": 5,
            "Harga Beli": 50000,
            "Harga Jual": 76000},
        "9781234567806": {
            "Judul": "Pendidikan Jasmani",
            "Penulis": "Geisha",
            "Stok": 1,
            "Harga Beli": 60000,
            "Harga Jual": 95000}
    }
    return inventaris

def simpan_kefile(inventaris, nama_file):
    with open(nama_file, "w") as file:
        for isbn, data in inventaris.items():
            file.write(f"{isbn},{data["Judul"]},{data["Penulis"]},{data["Stok"]},{data["Harga Beli"]},{data["Harga Jual"]}\n")
    print(f"File {nama_file} berhasil dibuat.")

def hitung_potensi_dan_update_data(inventaris):
    with open("laporan_inventaris.txt", "w") as file:
        for isbn, data in inventaris.items():
            keuntungan = (data["Harga Jual"] - data["Harga Beli"]) * data["Stok"]
            data["Potensi Keuntungan"] = keuntungan
            file.write(f"{isbn},{data["Judul"]},{data["Penulis"]},{data["Stok"]},{data["Harga Beli"]},{data["Harga Jual"]},{keuntungan}\n")
    print("File laporan_inventaris.txt berhasil dibuat.")

def analisis_inventaris(inventaris):
    print("\n Analisis Inventaris:")
    pertama = True
    total_inventaris = 0

    for isbn, data in inventaris.items():
        keuntungan = data["Potensi Keuntungan"]
        nilai_beli = data["Stok"] * data["Harga Beli"]
        total_inventaris += nilai_beli

        if pertama:
            tertinggi = (isbn, data)
            terendah = (isbn, data)
            pertama = False
        else:
            if keuntungan > tertinggi[1]["Potensi Keuntungan"]:
                tertinggi = (isbn, data)
            if keuntungan < terendah[1]["Potensi Keuntungan"]:
                terendah = (isbn, data)

    print(f" Buku dengan keuntungan tertinggi: {tertinggi[1]['Judul']} (Rp {tertinggi[1]['Potensi Keuntungan']})")
    print(f" Buku dengan keuntungan terendah : {terendah[1]['Judul']} (Rp {terendah[1]['Potensi Keuntungan']})")
    print(f" Total nilai inventaris (berdasarkan harga beli): Rp {total_inventaris}")
    print("\n Buku yang perlu direstock (stok < 5):")
    ada = False
    for isbn, data in inventaris.items():
        if data["Stok"] < 5:
            print(f"- {data['Judul']} (Stok: {data['Stok']})")
            ada = True
    if not ada:
        print("Tidak ada buku yang perlu direstock.")

inventaris = data_awal()
simpan_kefile(inventaris, "inventaris_buku.txt")
hitung_potensi_dan_update_data(inventaris)
analisis_inventaris(inventaris)