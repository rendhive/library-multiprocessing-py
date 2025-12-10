import multiprocessing

def print_square(n):
    print(f"Square of {n}: {n * n}")

if __name__ == "__main__":
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(print_square, range(10))

# Fungsi: Mengatur jumlah proses yang digunakan berdasarkan jumlah CPU yang ada.
# Kondisi: Ketika Anda ingin memanfaatkan semua core CPU untuk pemrosesan paralel.
