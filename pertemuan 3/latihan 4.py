class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        if not temp:
            print("null")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, list2):
        if not self.head:
            self.head = list2.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = list2.head


ll1 = LinkedList()
ll2 = LinkedList()

elemen1 = input("Masukkan elemen Linked List 1 (pisahkan dengan koma): ")
for data in elemen1.split(","):
    if data.strip():
        ll1.insert_at_end(int(data))

elemen2 = input("Masukkan elemen Linked List 2 (pisahkan dengan koma): ")
for data in elemen2.split(","):
    if data.strip():
        ll2.insert_at_end(int(data))

print("Linked List 1:")
ll1.display()

print("Linked List 2:")
ll2.display()

ll1.merge(ll2)

print("Linked List setelah digabungkan:")
ll1.display()