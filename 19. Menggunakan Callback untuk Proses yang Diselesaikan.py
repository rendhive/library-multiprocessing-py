import multiprocessing

def finished(result):
    print("Hasil dari proses:", result)

def multiply(n):
    return n * n

if __name__ == "__main__":
    pool = multiprocessing.Pool()
    result = pool.apply_async(multiply, (5,), callback=finished)  # Menggunakan callback
    pool.close()
    pool.join()

# Fungsi: Menggunakan callback untuk menangani hasil dari proses yang telah selesai.
# Kondisi: Ketika Anda ingin melakukan sesuatu setelah sebuah proses selesai.
