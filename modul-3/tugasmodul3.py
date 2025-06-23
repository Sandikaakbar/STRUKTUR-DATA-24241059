class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, capacity):
        self.top = None
        self.size = 0
        self.capacity = capacity

    def push(self, data):
        """Menambah elemen ke stack."""
        if self.is_full():
            print("Stack sudah penuh, tidak dapat menambah elemen.")
            return
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Stack: {self.display_stack()}")

    def pop(self):
        """Menghapus elemen dari stack."""
        if self.is_empty():
            print("Stack kosong, tidak ada elemen yang dapat dihapus.")
            return None
        removed_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(f"Elemen {removed_data} dihapus dari stack.")
        print(f"Stack: {self.display_stack()}")
        return removed_data

    def get_size(self):
        """Mencari tahu ukuran stack."""
        return self.size

    def peek(self):
        """Mencari tahu elemen puncak dari stack."""
        if self.is_empty():
            print("Stack kosong, tidak ada elemen puncak.")
            return None
        return self.top.data

    def is_full(self):
        """Mencari tahu apakah stack dalam kondisi penuh atau tidak."""
        return self.size == self.capacity

    def is_empty(self):
        """Mencari tahu apakah stack kosong."""
        return self.size == 0

    def display_stack(self):
        """Menampilkan elemen dalam stack."""
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements

def main():
    print("=====PROGRAM SEDERHANA UNTUK IMPLEMENTASI STACK DENGAN LINKED-LIST=====")
    capacity = int(input("Tentukan berapa kapasitas stack: "))
    stack = Stack(capacity)

    while True:
        print("\nPilih menu berikut ini:")
        print("1. Menambah isi stack")
        print("2. Menghapus isi stack")
        print("3. Cek Ukuran Stack saat ini")
        print("4. Cek Puncak Stack")
        print("5. Cek Stack Full")
        print("6. Keluar")

        choice = int(input("Masukkan pilihan anda: "))

        if choice == 1:
            data = int(input("Masukkan isi stack: "))
            stack.push(data)
            if not stack.is_full():
                continue_choice = input("Menambah isi Stack Pilih [Ya/Tidak]: ")
                if continue_choice.lower() != 'ya':
                    continue
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            print(f"Ukuran stack saat ini: {stack.get_size()}")
        elif choice == 4:
            top_element = stack.peek()
            if top_element is not None:
                print(f"Elemen puncak: {top_element}")
        elif choice == 5:
            print(f"Apakah stack penuh? {'Ya' if stack.is_full() else 'Tidak'}")
        elif choice == 6:
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
