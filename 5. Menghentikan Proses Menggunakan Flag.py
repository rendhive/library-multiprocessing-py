import multiprocessing
import time

def run(stop_event):
    while not stop_event.is_set():
        print("Proses berjalan...")
        time.sleep(1)

if __name__ == "__main__":
    stop_event = multiprocessing.Event()
    process = multiprocessing.Process(target=run, args=(stop_event,))
    process.start()

    time.sleep(3)  # Biarkan berjalan selama 3 detik
    stop_event.set()  # Menghentikan proses
    process.join()

print("Proses telah dihentikan.")
# Fungsi: Menggunakan Event untuk mengontrol eksekusi proses dan menghentikannya.
# Kondisi: Ketika Anda ingin menghentikan proses berdasarkan kondisi tertentu.
