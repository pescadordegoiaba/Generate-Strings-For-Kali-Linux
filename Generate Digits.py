import os
import random
import string
import time

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_to_file(size, code, destination_path):
    directory_name = f"{size}strings"
    create_directory_if_not_exists(os.path.join(destination_path, directory_name))

    filename = os.path.join(destination_path, directory_name, f"{size}strings.txt")
    with open(filename, 'a') as file:
        file.write(code + "\n")

    print(f"generate {size} strings: {code}")
    print(f"File saved in {filename}")

def main():
    destination_path = "/home/kali/Desktop/Generated-Digits/"

    sizes = [4, 6, 8, 16]

    while True:
        create_directory_if_not_exists(destination_path)

        size = random.choice(sizes)
        code = generate_random_string(size)
        save_to_file(size, code, destination_path)

        time.sleep(1)

if __name__ == "__main__":
    main()
