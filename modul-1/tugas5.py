def main():
    data_mahasiswa = {}

    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    for _ in range(jumlah):
        nim = input("\nNIM: ").strip()
        nama = input("Nama: ").strip()

        nilai_mata_kuliah = []
        while True:
            mk = input("Mata kuliah (ketik 'selesai' jika sudah selesai): ").strip()
            if mk.lower() == 'selesai':
                break
            nilai = float(input(f"Nilai {mk}: "))
            nilai_mata_kuliah.append((mk, nilai))

        data_mahasiswa[nim] = {'nama': nama, 'nilai': nilai_mata_kuliah}

    print("\nRekap Nilai Mahasiswa:")
    print("NIM\t\tNama\t\tRata-rata")
    for nim, info in data_mahasiswa.items():
        nilai_list = info['nilai']
        rata = sum(nilai for _, nilai in nilai_list) / len(nilai_list) if nilai_list else 0
        print(f"{nim}\t{info['nama']}\t{rata:.2f}")

    print("\nData Lengkap Mahasiswa:")
    for nim, info in data_mahasiswa.items():
        print(f"NIM: {nim}, Nama: {info['nama']}, Nilai: {info['nilai']}")

if __name__ == "__main__":
    main()
