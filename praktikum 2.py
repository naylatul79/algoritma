#=========================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 1 : Membuat Fungsi Load Data dari File 
#=========================================================================

#Variabel menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict ={} # inisialisasi data dictionary
    with open(nama_file,"r", encoding="utf-8") as file:
        for baris in file :
            baris = baris.strip()
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim]= {"nama" : nama, "nilai" : int(nilai)} #masukkan dalam dict
        return data_dict
    
#buka_data =baca_data(nama_file) #memanggil fungsi load data dan menyimpan dalam variabel
#print("jumlah data terbaca", len(buka_data)) #melihat berapa data yang di load



#=========================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 2 : Membuat fungsi menampilkan data 
#=========================================================================

def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n========= DAFTAR MAHASISWA =========")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' :>5}")
    '''

    untuk tampilan yang rapi, atur lebar kolom
    {'NIM :<10 } artinya nim rata kiri dengan lebar kolom 12 karakter
    {'Nilai : >5} artinya nilai rata kanan dengan lebar kolom 5 karakter

    '''
    print("-"*35) #membuat garis

    #menampilkan isi datanya
    for nim in sorted (data_dict.keys()) :
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")

#tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#=========================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 3 : Membuat fungsi mencari data 
#=========================================================================

#membuat fungsi prncarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dec 
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict :
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("============ Data Mahasiswa Ditemukan ============")
        print(f"NIM : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else :
        print("Data tidak ditemukan. Pastukan NIM yang dimasukkan benar")

#memanggil fungsi cari data
#cari_data(buka_data)

#=========================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 4 : Membuat fungsi Update Data
#=========================================================================

#membuat fungsi update data 
def ubah_data(data_dict):

    #awali dulu dengan mencari nim / data mahasiswa yang ingin di update
    nim = input("masukkan NIM mahasiswa yang ingin diubah datanya : ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan/ Update dibatalkan.")
        return
    
    try :
        nilai_baru = int(input("masukkan nilai baru 0-100 : ").strip())
    except ValueError :
        print("Nilai harus berupa angka. Update Dibatalkan.")

    if nilai_baru < 0 or nilai_baru >100:
        print("Nilai harus 0 sampai 100. Update dibatalkan.")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru 

    print(f"Update Berhasil . Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi ubah data 
#ubah_data(buka_data)

#=========================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 5 : Membuat fungsi menyimpan Data pada file
#=========================================================================

#mambuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict) :
    with open(nama_file, "w",encoding="utf-8") as file :
         for nim in sorted(data_dict.keys()) :
             nama = data_dict[nim]["nama"]
             nilai = data_dict[nim]["nilai"]
             file.write(f"{nim},{nama},{nilai}")

#memanggil fungsi simpan data 
#simpan_data(nama_file,buka_data)
#print("\nData Berhasil disimpan ke file:", nama_file)


#=========================================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 5 : Membuat fungsi menyimpan Data pada file
#=========================================================================

def main ():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file) #fs.1 fungsi load data

    while True :
        print("\n===== MENU DATA MAHASISWA =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mhasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1" :
            tampilkan_data(buka_data) #fs 2 menampilkan data

        elif pilihan == "2" :
            cari_data(buka_data) #memanggil fs. 3 mecari data
        
        elif pilihan == "3" :
            ubah_data(buka_data) #memanggil fs 4 mengubah data

        elif pilihan == "4" :
            simpan_data(nama_file, buka_data) #memanggil fs 5 menyimpan data ke file
            print("Data berhasil disimpan")

        elif pilihan == "0":
            print("Program Selesai")
            break

        else : 
            print("Pilihan tidak valid. Silahkan coba lagi")

if __name__ == "__main__":
    main()
