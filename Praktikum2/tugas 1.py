# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama :Naylatul Fadhilah
# NIM : J0403251033
# Kelas : TPL P1

# ==========================================================
# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file = "stok_barang.txt" #menyimpan nama file data stok barang


# -------------------------------
# Fungsi 1: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """

    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    
    Output:
    - stok_dict (dictionary)
    key = kode_barang
    value = {"nama_barang": nama_barang, "stok": stok_int}

    """

    stok_dict = {} #inisialisasi dictionary kosong untuk menyimpan data stok
    with open(nama_file,"r", encoding="utf-8") as file: 
        for baris in file :       #membaca setiap baris dalam file
            baris = baris.strip()     #menghapus spasi atau karakter newline di awal/akhir baris
            kode_barang, nama_barang, stok = baris.split(",")      #memisahkan data berdasarkan koma
            stok_dict[kode_barang] = {           #menyimpan data ke dictionary
                "nama_barang": nama_barang,   #menyimpan nama barang
                "stok": int(stok)}            #menyimpan stok sebagai integer
    return stok_dict    #mengembalikan dictionary berisi data stok


#buka_data = baca_stok(nama_file)
#print("jumlah data terbaca", len(buka_data))

# -------------------------------
# Fungsi 2: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):  
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """

    with open(nama_file, "w",encoding="utf-8") as file :  #membuka file dalam mode tulis
         for kode_barang in sorted(stok_dict.keys()) :   #mengurutkan kode barang secara alfabetis
             nama_barang = stok_dict[kode_barang]["nama_barang"]    #mengambil nama barang dari dictionary
             stok = stok_dict[kode_barang]["stok"]          #mengambil stok dari dictionary
             file.write(f"{kode_barang},{nama_barang},{stok}\n")    #menulis data ke file sesuai format

    
# (baris pemanggilan simpan data yang salah dihapus)
#simpan_stok(nama_file, buka_data)



# -------------------------------
# Fungsi 3: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua data stok dalam format tabel.                 
    """

    #Membuat header tabel
    print("\n============== DAFTAR BARANG ==============")
    print(f"{'kode_barang' : <10} | {'nama_barang' : <12} | {'stok' :>5}") #membuat header tabel
    '''

    untuk tampilan yang rapi, atur lebar kolom
    {'kode_barang :<10 } artinya kode_barang rata kiri dengan lebar kolom 12 karakter
    {'stok : >5} artinya stok rata kanan dengan lebar kolom 5 karakter

    '''
    print("-"*35) #membuat garis

    #menampilkan isi datanya
    for kode_barang in sorted(stok_dict.keys()) :  #mengurutkan kode barang secara alfabetis
        nama_barang = stok_dict[kode_barang]["nama_barang"]    #mengambil nama barang dari dictionary
        stok = stok_dict[kode_barang]["stok"]          #mengambil stok dari dictionary
        
        print(f"{kode_barang:<10} | {nama_barang:<12} | {int(stok):>5}")    #menampilkan data dalam format tabel dengan rapi



#tampilkan_semua(buka_data) #memanggil fungsi untuk menampilkan data

# -------------------------------
# Fungsi 4 : Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode_barang_cari = input("Masukkan kode barang yang dicari: ").strip()  #mengambil input kode barang dari user dan menghapus spasi di awal/akhir
   
    if kode_barang_cari in stok_dict:    #memeriksa apakah kode barang ada dalam dictionary
        nama_barang = stok_dict[kode_barang_cari]["nama_barang"]          #mengambil nama barang dari dictionary
        stok = stok_dict[kode_barang_cari]["stok"]              #mengambil stok dari dictionary

        #menampilkan data barang yang ditemukan
        print("============ Barang Ditemukan ============")
        print(f"kode_barang : {kode_barang_cari}")
        print(f"nama_barang : {nama_barang}")
        print(f"stok        : {stok}")
    else:       #jika kode barang tidak ditemukan
        print("Barang dengan kode tersebut tidak ditemukan. Pastikan kode benar.") 

#cari_barang(buka_data) #memanggil fungsi untuk mencari data 


# -------------------------------
# Fungsi 5: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip()   #mengambil input kode barang dari user dan menghapus spasi di awal/akhir
    #validasi input
    if not kode:
        print("Kode tidak boleh kosong.")
        return
    
    #validasi kode tidak boleh sama
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return
    nama = input("Masukkan nama barang: ").strip()     #mengambil input nama barang dari user dan menghapus spasi di awal/akhir
    
    #validasi input nama tidak boleh kosong
    if not nama:
        print("Nama tidak boleh kosong.")
        return
    try:
        stok_awal = int(input("Masukkan stok awal (angka): ").strip())  #mengambil input stok awal dari user dan menghapus spasi di awal/akhir
        if stok_awal < 0:     #validasi stok tidak boleh negatif
            print("Stok tidak boleh negatif.")
            return
    except ValueError:   #input stok harus berupa angka
        print("Input stok harus berupa angka.")
        return
    
    #konfirmasi penambahan barang
    print(f"Akan menambahkan: {kode} | {nama} | stok {stok_awal}")
    konfirm = input("Lanjutkan? (y/n): ").strip().lower()
    
    if konfirm != 'y':
        print("Dibatalkan.")
        return
    
    #menambahkan barang ke dictionary
    stok_dict[kode] = {"nama_barang": nama, "stok": stok_awal}
    print("Barang berhasil ditambahkan.")
    return

# -------------------------------
# Fungsi 6: Update stok barang
# -------------------------------
def update_stok(stok_dict):     
    """

    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    
    """
    kode_barang = input("Masukkan kode barang yang ingin diupdate: ").strip()    #mengambil input kode barang dari user dan menghapus spasi di awal/akhir
    
    #mengecek apakah kode barang ada dalam dictionary
    if kode_barang not in stok_dict:
        print("Kode tidak ditemukan.")
        return
    
    #menampilkan pilihan update stok
    print("Pilih jenis update stok:")   
    print("1. Tambah Stok")
    print("2. Kurangi Stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()   #mengambil input pilihan dari user dan menghapus spasi di awal/akhir

    try:
        jumlah = int(input("Masukkan jumlah stok baru (angka): ").strip())   #meminta input stok baru dari user dan menghapus spasi di awal/akhir
    except ValueError:
        print("Input stok harus berupa angka. Update dibatalkan.")
        return
    
    if jumlah < 0:
        print("Jumlah stok tidak boleh negatif. Update dibatalkan.")
        return
    
    stok_lama = stok_dict[kode_barang]["stok"]    #mengambil stok lama dari dictionary

    if pilihan == "1":    #jika memilih untuk menambah stok
        stok_dict[kode_barang]["stok"] = stok_lama + jumlah
        print(f"Stok berhasil ditambah. Stok baru: {stok_dict[kode_barang]['stok']}")

    elif pilihan == "2":  #jika memilih untuk mengurangi stok
        if stok_lama - jumlah < 0:
            print("Stok tidak boleh negatif. Update dibatalkan.")
            return
        stok_dict[kode_barang]["stok"] = stok_lama - jumlah
        print(f"Stok berhasil dikurangi. Stok baru: {stok_dict[kode_barang]['stok']}")
    else:
        print("Pilihan tidak valid. Update dibatalkan.")
        
    

#update_stok(buka_data) #memanggil fungsi untuk mengupdate data
    
# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    buka_data = baca_stok(nama_file)
    
    # Menu interaktif
    while True:
        print("\n================ STOK BARANG ==================")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang Berdasarkan Kode Barang")
        print("3. Tambah Barang Baru")
        print("4. Update Stok Barang")
        print("5. Simpan ke File")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()   #mengambil input pilihan menu dari user dan menghapus spasi di awal/akhir

        # Menangani pilihan menu
        if pilihan == "1":                        #fungsi 1 untuk menampilkan semua barang
            tampilkan_semua(buka_data)

        elif pilihan == "2":                      #fungsi 2 untuk mencari barang berdasarkan kode
            cari_barang(buka_data)

        elif pilihan == "3":                      #fungsi 3 untuk menambah barang baru
            tambah_barang(buka_data)

        elif pilihan == "4":                      #fungsi 4 untuk mengupdate stok barang
            update_stok(buka_data)

        elif pilihan == "5":
            simpan_stok(nama_file, buka_data)     #fungsi 5 untuk menyimpan data ke file
            print("Data berhasil disimpan.")
            
        elif pilihan == "0":     #keluar dari program
            print("Program selesai.")
            break

        else:    #pilihan tidak valid
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()