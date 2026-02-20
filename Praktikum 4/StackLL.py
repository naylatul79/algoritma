#===================================================================================================
#Nama    : Naylatul Fadhilah
#NIM     : J0403251033
#Kelas   : TPL A1
#===================================================================================================

#===================================================================================================
#Implementasi Dasar : Stack
#===================================================================================================


class Node:
    #konstruktor yang dijalankan secara otomatis ketika claas Node dipanggil / diinstansiasi
    def __init__(self, data):
        self.data = data    #menyimpan nilai atau data pada list
        self.next = None    #pointer ini menunjuk ke note berikitnya (awal=none)


#stack ada operasi push(memasukkan head  baru) dan pop (menghapus head) 

class Stack:
    def __init__(self):
        self.top = None  #top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None  #stack kosong jika top menunjuk ke None
    
    def push(self, data):      #memasukkan data baru ke stack
        #1 membuat node baru
        nodeBaru = Node(data)  #instansiasi/memanggil konstruktor pada class Node

        #2 node baru menunjuk ke top yang kama (head lama)
        nodeBaru.next = self.top  

        #3 geser top pindah ke node baru 
        self.top = nodeBaru


    def pop(self): #mengambil / menghapus node paling atas (top/head)
        
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None 
        data_terhapus = self.top.data      #soroti bagian top dan simpan di variabel
        self.top = self.top.next           #geser top ke node berikutnya
        return data_terhapus  
    
    def peek(self):
        #melihat data pada top tanpa menghapusnya
        if self.is_empty():
            return None
        return self.top.data  

    def tampilkan(self):
        current = self.top  
        print("Top -> " ,  end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Instansiasi class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top): ", s.peek())