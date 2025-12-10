import multiprocessing

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    numbers = [0, 1, 2, 3, 4, 5]
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(factorial, numbers)

    print("Faktorial dari angka:", results)
# Fungsi: Menghitung faktorial dari sejumlah angka menggunakan Pool.
# Kondisi: Ketika Anda ingin menerapkan fungsi yang sama ke banyak elemen dalam list.
