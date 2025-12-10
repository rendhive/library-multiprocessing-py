import multiprocessing
import time

semaphore = multiprocessing.Semaphore(3)  # Maksimal 3 proses yang berjalan bersamaan

def limited_worker(n):
    with semaphore:
        print(f"Proses {n} memulai...")
        time.sleep(2)
        print(f"Proses {n} selesai.")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=limited_worker, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# Fungsi: Menggunakan semaphore untuk membatasi jumlah proses yang dapat berjalan bersamaan.
# Kondisi: Ketika Anda memiliki resource yang terbatas yang tidak dapat diakses oleh semua proses pada satu waktu.
