class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    def delete_node(self, key):
        temp = self.head
        if not temp:
            print("linked list kosong")
            return
        if temp.data == key:
            self.head = temp.next
            print(f"elemen {key} berhasil dihapus")
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            print(f"elemen {key} tidak ditemukan")
            return
        prev.next = temp.next
        print(f"elemen {key} berhasil dihapus")
        
data = linkedlist()
data_input = [10, 20, 30, 40, 50]
for item in data_input:
        data.insert(item)
print("Isi linked list:")
data.display()
hapus = int(input("Masukkan elemen yang ingin dihapus: "))
data.delete_node(hapus)
print("Isi linked list setelah penghapusan:")
data.display()