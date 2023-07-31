import os
import random
import string
import time
import concurrent.futures
import threading

def generate_random_string_v2(length):
    characters = string.ascii_letters + string.digits
    code_type = random.randint(1, 4)

    if code_type == 1:
        characters = string.ascii_lowercase
    elif code_type == 2:
        characters = string.ascii_uppercase
    elif code_type == 3:
        characters = string.ascii_letters

    return ''.join(random.choice(characters) for _ in range(length))

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def check_existing_code(size, code, destination_path):
    directory_name = f"{size}strings"
    file_path = os.path.join(destination_path, directory_name, f"{size}strings.txt")

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == code:
                    return True

    return False

# Cria um semáforo para controlar o acesso ao recurso compartilhado (arquivos)
file_semaphore = threading.Semaphore()

def save_to_file(size, code, destination_path):
    directory_name = f"{size}strings"
    create_directory_if_not_exists(os.path.join(destination_path, directory_name))

    filename = os.path.join(destination_path, directory_name, f"{size}strings.txt")

    if not check_existing_code(size, code, destination_path):
        with file_semaphore:
            with open(filename, 'a') as file:
                file.write(code + "\n")

            print(f"generate {size} strings: {code}")
            print(f"File saved in {filename}")
    else:
        print(f"Code {code} already exists. Generating a new one.")

def generate_and_save(sizes, destination_path):
    while True:
        size = random.choice(sizes)
        code = generate_random_string_v2(size)
        save_to_file(size, code, destination_path)
        time.sleep(1)

def main():
    destination_path = "/home/kali/Desktop/Generated-Digits/"
    num_threads = int(input("Enter the number of threads: "))

    sizes = [4, 6, 8, 16]

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(generate_and_save, sizes, destination_path) for _ in range(num_threads)}
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
