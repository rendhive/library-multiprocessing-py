import multiprocessing
import time

def countdown(n):
    while n > 0:
        print(f"Countdown: {n}")
        n -= 1
        time.sleep(1)

if __name__ == "__main__":
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=countdown, args=(5,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# Fungsi: Membuat dan menjalankan beberapa proses secara bersamaan.
# Kondisi: Ketika Anda memiliki beberapa tugas yang dapat dijalankan secara paralel.
