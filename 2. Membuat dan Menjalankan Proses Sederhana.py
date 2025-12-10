import multiprocessing

def worker():
    print("Proses sedang berjalan!")

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()

# Fungsi: Membuat dan menjalankan proses untuk tugas tertentu.
# Kondisi: Ketika Anda ingin mendelegasikan tugas ke proses terpisah.
