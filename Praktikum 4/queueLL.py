#===================================================================================================
#Nama    : Naylatul Fadhilah
#NIM     : J0403251033
#Kelas   : TPL A1
#===================================================================================================

#===================================================================================================
#Implementasi Dasar : Queue
#===================================================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika claas Node dipanggil / diinstansiasi
    def __init__(self, data):
        self.data = data    #menyimpan nilai atau data pada list
        self.next = None    #pointer ini menunjuk ke note berikitnya (awal=none)

class Queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None  #node paling depan 
        self.rear = None   #node paling belakang 
    
    def is_empty(self):
        return self.front is None  

    #membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self, data):
        nodeBaru = Node(data)  
        
        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queue tidak kosong, maka Letakkan data baru ke setelah rear dan jadikan data baru sebagai rear 
        self.rear.next = nodeBaru  #letakkan data baru pada setelahnya rear
        self.rear = nodeBaru        #Jadikan data baru sebagai rear


    def dequeue(self):
        #menghapus data dari depam / front
        data_terhapus = self.front.data  #lihat data paling depan

        #geser front ke node berikutnya
        self.front = self.front.next      

        #Jika setelah geser front menjadi None, maka queue kosong, 
        #rear juga harus jadi none
        if self.front is None:
            self.rear = None

    def tampilkan(self):
        current = self.front  
        print("Front -> " ,  end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(" Rear")

#instansiasi class Queue 
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")  
q.tampilkan()
q.dequeue()
q.tampilkan()   
        