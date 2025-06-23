# Membuat Stack
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print ("Stack : ", stack)

# pop 
if len(stack) != 0:
    print("Pop : ", stack.pop())
    print("Stack : ", stack)
else :
    print("Stack Kosong!")

# top/peek
if not bool(stack):
    print("Stack Kosong!")
else:
    print("stack : ", stack)
    print("Top/Peek : ", stack[-1])


# isEmpty
if not bool(stack):
    print("Stack Kosong ")
else :
    print("Stack tidak kosong! ", stack)


# size
print("Stack Size : ", len(stack))


# Membuat program untuk menerima input dari pengguna untuk operasi push dan pop stack
# langkah 1 menyiapkan stack array
tumpukan = []

# langkah 2 push elemen ke stack
while True:
    isi_elemen = input("Masukkan isi elemen (ketik Selesai jika tidak): ")
    if isi_elemen.lower() == 'selesai':
        break
    stack = tumpukan.append(int(isi_elemen))
    print("tumpukan : ", tumpukan)

# langkah 3 pop elemen dari stack
for i in range(len(tumpukan)):
    if len(tumpukan) != 0:
        hapus = input('Apakah ingin menghapus elemen [ya/tidak] : ')
        if hapus.lower() == 'tidak' :
            break
        print("Pop : ", tumpukan.pop())
        print("tumpukan : ", tumpukan)
    else :
        print("Stack Kosong!")
        
        
def buat_node(data):
    return {'data': data, 'next': None}

def push(head, data):
    new_node = buat_node(data)
    new_node['next'] = head
    return new_node

def pop(head):
    if head is None:
        print("Stack kosong.")
        return None, None
    popped = head['data']
    head = head['next']
    return head, popped

def peek(head):
    if head is None:
        return None
    return head['data']

def is_empty(head):
    return head is None

# Uji coba
stack = None  # Stack awal kosong

stack = push(stack, 10)
stack = push(stack, 20)
stack = push(stack, 30)

print("Top stack:", peek(stack))  # Harusnya 30

stack, val = pop(stack)
print("Pop:", val)               # Harusnya 30

stack, val = pop(stack)
print("Pop:", val)               # Harusnya 20

print("Top stack sekarang:", peek(stack))  # Harusnya 10