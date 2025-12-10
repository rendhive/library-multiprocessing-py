import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(10))  # Menghitung kuadrat angka 0-9

    print("Hasil kuadrat:", results)
# Fungsi: Menggunakan Pool untuk menjalankan fungsi dalam beberapa proses.
# Kondisi: Ketika Anda memiliki banyak tugas dengan fungsi yang sama dan ingin memanfaatkannya secara paralel.
