import multiprocessing

def cube(n):
    return n ** 3

if __name__ == "__main__":
    with multiprocessing.Pool(processes=2) as pool:
        result = pool.apply(cube, (3,))  # Menghitung kubus dari 3

    print("Hasil kubus dari 3:", result)
# Fungsi: Menggunakan Pool untuk melakukan panggilan fungsi dalam proses paralel.
# Kondisi: Ketika Anda memiliki satu pekerjaan yang ingin dilakukan di dalam proses.
