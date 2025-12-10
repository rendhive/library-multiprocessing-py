import multiprocessing

def worker(queue):
    queue.put("Hello from worker!")

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=worker, args=(queue,))
    process.start()
    message = queue.get()  # Mengambil pesan dari worker
    process.join()

    print("Pesan dari worker:", message)
# Fungsi: Menggunakan Queue untuk mengirim data antar-proses.
# Kondisi: Ketika Anda perlu mengirim data dari satu proses ke proses lain.
