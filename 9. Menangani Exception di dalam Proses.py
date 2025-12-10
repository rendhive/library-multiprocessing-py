import multiprocessing

def risky_task():
    raise ValueError("Something went wrong!")

if __name__ == "__main__":
    process = multiprocessing.Process(target=risky_task)

    try:
        process.start()
        process.join()
    except Exception as e:
        print(f"Error caught: {e}")

# Fungsi: Menangani exception yang terjadi dalam proses.
# Kondisi: Ketika Anda perlu memastikan bahwa error dalam proses dapat ditangkap dan ditangani.
