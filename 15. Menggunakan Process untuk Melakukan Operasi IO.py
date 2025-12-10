import multiprocessing
import time

def io_bound_task(n):
    print(f"Task {n} mulai...")
    time.sleep(3)  # Simulasi operasi I/O
    print(f"Task {n} selesai.")

if __name__ == "__main__":
    processes = []
    for i in range(4):
        process = multiprocessing.Process(target=io_bound_task, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# Fungsi: Melakukan operasi I/O menggunakan multiprocessing.
# Kondisi: Ketika Anda ingin menjalankan operasi yang mungkin memakan waktu karena I/O pada beberapa proses secara paralel.
