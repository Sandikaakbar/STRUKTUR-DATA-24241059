def main():
    data_customer = {}

    jumlah = int(input("Masukkan jumlah barang: "))
    for _ in range(jumlah):
        nama = input("\tanggal belanja: ").strip()
        harga = input("harga: ").strip()
        kuality = input("kualitas barang: ").strip()

        total_belanja = []
        while True:
            mk = input("nama barang (ketik 'selesai' jika sudah selesai): ").strip()
            if mk.lower() == 'selesai':
                break
            nilai = float(input(f"harga {mk}: "))
            total_belanja.append((mk, nilai))

        data_customer[tanggal_belanja] = {'harga': harga, 'nilai': tanggal_belanja}

    print("\nRekap total belanja:")
    print("NIM\t\tNama\t\tRata-rata")
    for tanggal_belanja, info in data_customer.items():
        nilai_list = info['nilai']
        rata = sum(nilai for _, nilai in nilai_list) / len(nilai_list) if nilai_list else 0
        print(f"{nama}\t{info['nama']}\t{rata:.2f}")

    print("\nData Lengkap Mahasiswa:")
    for nama, info in data_customer.items():
        print(f"NIM: {nama}, Nama: {info['nama']}, Nilai: {info['nilai']}")

if __name__ == "__main__":
    main() 