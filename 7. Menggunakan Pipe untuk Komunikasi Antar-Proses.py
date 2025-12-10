import multiprocessing

def worker(conn):
    conn.send("Hello from worker!")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    process = multiprocessing.Process(target=worker, args=(child_conn,))
    process.start()
    message = parent_conn.recv()  # Menerima pesan dari worker
    process.join()

    print("Pesan dari worker:", message)
# Fungsi: Menggunakan Pipe untuk komunikasi dua arah antar-proses.
# Kondisi: Ketika Anda memerlukan saluran komunikasi langsung antara dua proses.
