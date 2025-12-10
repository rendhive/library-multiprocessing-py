import multiprocessing

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    process = multiprocessing.Process(target=greet, args=("Alice",))
    process.start()
    process.join()

# Fungsi: Menggunakan argumen saat membuat proses.
# Kondisi: Ketika Anda perlu menyampaikan data ke fungsi yang akan dijalankan di proses.
