import multiprocessing

def worker():
    print("Worker sedang bekerja...")

if __name__ == "__main__":
    with multiprocessing.get_context("spawn").Pool() as pool:
        pool.apply(worker)

# Fungsi: Menggunakan konteks untuk mengontrol cara proses baru dibentuk.
# Kondisi: Ketika Anda ingin mengontrol mode pembuatan proses untuk kompatibilitas dengan sistem lain.
