import multiprocessing
import time

def worker(barrier):
    print("Proses menunggu di barrier.")
    barrier.wait()  # Menunggu proses lain
    print("Proses melanjutkan setelah barrier!")

if __name__ == "__main__":
    num_processes = 3
    barrier = multiprocessing.Barrier(num_processes)

    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(target=worker, args=(barrier,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# Fungsi: Menggunakan barrier untuk menyinkronkan beberapa proses.
# Kondisi: Ketika Anda ingin menunggu sejumlah proses mencapai titik tertentu sebelum melanjutkan.
