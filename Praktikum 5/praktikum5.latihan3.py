# ==========================================================
# # Nama : Naylatul Fadhilah
# NIM  : J0403251033
# Kelas : TPL A1/P1 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
# Fungsi cari_maks(data, index) digunakan untuk mencari nilai maksimum
# dalam sebuah list menggunakan metode rekursif.

def cari_maks(data, index=0): 
 
    # Base case 
    # Jika index sudah mencapai panjang list, maka kita berhenti dan
    # mengembalikan nilai pada index terakhir sebagai nilai maksimum.
    if index == len(data) - 1: 
        return data[index] 
 
    # Recursive case 
    # cari nilai maksimum dari sisa list setelah index saat ini
    maks_sisa = cari_maks(data, index + 1) 
    
    # Bandingkan nilai saat ini dengan nilai maksimum dari sisa list
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        return maks_sisa 
 
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka)) 