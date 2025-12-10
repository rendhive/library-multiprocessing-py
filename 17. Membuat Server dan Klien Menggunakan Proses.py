import multiprocessing
import socket

def server_program():
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from:", address)
    conn.send(b'Hello, Client!')
    conn.close()

if __name__ == "__main__":
    server_process = multiprocessing.Process(target=server_program)
    server_process.start()
    
    # Klien terpisah
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 5000))
    message = client_socket.recv(1024)
    print("Message from server:", message.decode())
    
    client_socket.close()
    server_process.join()
# Fungsi: Menciptakan server dan klien sederhana menggunakan multiprocessing untuk komunikasi jaringan.
# Kondisi: Ketika Anda perlu menjalankan server pada proses terpisah dari klien.
