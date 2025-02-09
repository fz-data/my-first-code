"""
ini adalah demo project pertama dengan python
"""


def main():
    print("=== Program Kasir Sederhana ===")

    # Daftar untuk menyimpan item yang dibeli
    items = []

    while True:
        # Input nama barang
        nama_barang = input("Masukkan nama barang (atau ketik 'selesai' untuk mengakhiri): ")
        if nama_barang.lower() == 'selesai':
            break

        # Input harga barang
        harga_barang = float(input("Masukkan harga barang: "))

        # Input jumlah barang
        jumlah_barang = int(input("Masukkan jumlah barang: "))

        # Hitung total harga untuk item ini
        total_harga = harga_barang * jumlah_barang

        # Simpan item ke dalam daftar
        items.append({
            'nama': nama_barang,
            'harga': harga_barang,
            'jumlah': jumlah_barang,
            'total': total_harga
        })

    # Tampilkan struk belanja
    print("\n=== Struk Belanja ===")
    total_semua = 0
    for item in items:
        print(f"{item['nama']} - Harga: {item['harga']} x Jumlah: {item['jumlah']} = Total: {item['total']}")
        total_semua += item['total']

    print(f"\nTotal Semua: {total_semua}")
    print("=======================")


if __name__ == "__main__":
    main()