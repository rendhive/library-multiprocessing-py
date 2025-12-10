import multiprocessing

def update_value(shared_dict):
    shared_dict['value'] = 'Updated value'

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        shared_dict = manager.dict()
        shared_dict['value'] = 'Original value'
        
        process = multiprocessing.Process(target=update_value, args=(shared_dict,))
        process.start()
        process.join()

        print("Value setelah diperbarui:", shared_dict['value'])
# Fungsi: Menggunakan Manager untuk berbagi objek antara proses.
# Kondisi: Ketika Anda perlu berbagi data kompleks antara beberapa proses.
