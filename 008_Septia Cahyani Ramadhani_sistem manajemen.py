stok_barang = 100

def kurangi_stok(stok_barang, total):
    if total <= stok_barang:
        stok_barang -= total
        print(f"{total} telah dilakukan. Total stok: {stok_barang}")
        return stok_barang # Mengembalikan stok yang diperbarui
    else:
        print("Stok tidak cukup! Transaksi tidak dapat dilakukan.")
        return stok_barang # Mengembalikan stok asli

print("Sistem manajemen stok barang toko")

while True:
    total = int(input("Masukkan jumlah barang yang ingin dikurangi: "))
    stok_barang = kurangi_stok(stok_barang, total) # Memperbarui stok_barang
    lanjut = input("apakah anda ingin melanjutkan transaksi (ya/tidak): ").lower()
    if lanjut == "tidak":
        print ("Transaksi telah selesai. terima kasih!")
        break

