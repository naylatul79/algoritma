#===============================================================================    
#Nama    : Naylatul Fadhilah
#NIM     : J0403251033
#Kelas   : TPL A1
#===============================================================================

#================================================================================
#Implementasi Dasar : Node pada linked list
#================================================================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika claas Node dipanggil / diinstansiasi
    def __init__(self, data):
        self.data = data    #menyimpan nilai atau data pada list
        self.next = None    #pointer ini menunjuk ke note berikitnya (awal=none)

#1)membuat node dengan instansiasi class Node
NodeA = Node("A")
NodeB = Node("B")
NodeC = Node("C")

#2) Menghubungkan Node : A -> B -> C -> None
head = NodeA

#3) Traversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data)  #menampilkan data pada node saat ini
    current = current.next  #pindah ke node berikutnya