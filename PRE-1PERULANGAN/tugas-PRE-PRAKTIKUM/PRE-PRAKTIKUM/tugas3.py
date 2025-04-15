def fibonacci(n):
    fib_list = []
    a, b = 0, 1  # Inisialisasi dua angka pertama dalam deret Fibonacci
    for _ in range(n):
        fib_list.append(b)  # Menambahkan angka Fibonacci ke dalam daftar
        a, b = b, a + b  # Menghitung angka Fibonacci berikutnya
    return fib_list

# Meminta input jumlah deret dari pengguna
jumlah_deret = int(input("Masukkan jumlah deret Fibonacci: "))

# Menghasilkan dan menampilkan deret Fibonacci
deret_fibonacci = fibonacci(jumlah_deret)
print("Deret Fibonacci:", ', '.join(map(str, deret_fibonacci)))