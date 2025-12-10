import multiprocessing

def double(n):
    return n * 2

if __name__ == "__main__":
    with multiprocessing.Pool(processes=3) as pool:
        for result in pool.imap(double, range(5)):  # Memproses data dengan cara mendekati stream
            print(result)
# Fungsi: Menggunakan imap untuk memproses data satu per satu secara stream.
# Kondisi: Ketika Anda ingin memproses data besar secara efisien dan mendapatkan hasil secara bertahap.
