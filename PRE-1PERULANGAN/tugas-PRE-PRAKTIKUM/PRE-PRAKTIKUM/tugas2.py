# Meminta input jumlah deret dari pengguna
jumlah_deret = int(input("Masukkan jumlah deret: "))

# Daftar untuk menyimpan bilangan genap
Angka_list = []

# Menghasilkan bilangan genap
for i in range(1, jumlah_deret // 2 + 1):
    Angka_list.append(i * 2)

# Menampilkan bilangan genap
print("Bilangan genap:", Angka_list)

# Menampilkan setiap bilangan genap dengan loop
for i in Angka_list:
    print(f"Bilangan genap sekarang -> {i}")

print("Loop berakhir")
