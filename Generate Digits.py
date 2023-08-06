#!/usr/bin/env python3

import os
import random
import string
import time
import concurrent.futures
import threading
from pathlib import Path
import requests

# Constantes para os tipos de geração
GENERATE_RANDOM_DIGITS = 1
GENERATE_RANDOM_PASSWORDS = 2
GENERATE_RANDOM_WORDS = 3
GENERATE_ALL = 4

# API URL para a Random Word API
RANDOM_WORD_API_URL = "https://random-word-api.herokuapp.com/word?number=1"

# Cria um semáforo para controlar o acesso ao recurso compartilhado (arquivos)
file_semaphore = threading.Semaphore()

def has_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def generate_random_string_v2(length):
    characters = string.ascii_letters + string.digits
    code_type = random.randint(1, 4)

    if code_type == 1:
        characters = string.digits
    elif code_type == 2:
        characters = string.ascii_letters
    elif code_type == 3:
        characters = string.ascii_lowercase

    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_real_word_password():
    try:
        response = requests.get(RANDOM_WORD_API_URL)
        if response.status_code == 200:
            data = response.json()
            word = data[0]
            return word
    except requests.RequestException:
        pass

    print(f"Failed to get a real word. Using random characters instead.")
    return generate_random_string_v2(10)

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

def check_existing_codes_in_thread(destination_path, generation_type, num_codes_to_check):
    sizes = [4, 6, 8, 16]
    codes_to_check = []
    while num_codes_to_check > 0:
        size = random.choice(sizes)
        code = generate_and_save(size, destination_path, generation_type, False)
        if code not in codes_to_check:
            codes_to_check.append(code)
            num_codes_to_check -= 1

    existing_codes = []
    for code in codes_to_check:
        if check_existing_code(len(code), code, destination_path):
            existing_codes.append(code)

    print(f"Existing codes of size {sizes}: {existing_codes}")

def save_to_file(size, code, destination_path):
    directory_name = f"{size}strings"
    create_directory_if_not_exists(os.path.join(destination_path, directory_name))

    filename = os.path.join(destination_path, directory_name, f"{size}strings.txt")

    if not check_existing_code(size, code, destination_path):
        with file_semaphore:
            with open(filename, 'a') as file:
                file.write(code + "\n")

        print(f"Generated {size}-character string: {code}")
        print(f"File saved in {filename}")
    else:
        print(f"Code {code} already exists. Generating a new one.")

def generate_and_save(size, destination_path, generation_type, should_save=True):
    if generation_type == GENERATE_RANDOM_DIGITS:
        code = generate_random_string_v2(size)
    elif generation_type == GENERATE_RANDOM_PASSWORDS:
        if has_internet_connection():
            code = generate_real_word_password()
        else:
            code = generate_random_password(size)
    elif generation_type == GENERATE_RANDOM_WORDS:
        code = generate_real_word_password()
    else:
        raise ValueError("Invalid generation type.")

    if check_existing_code(size, code, destination_path):
        print(f"Code {code} already exists.")
        return

    if should_save:
        save_to_file(size, code, destination_path)

    return code

def main():
    destination_path = Path("/home/kali/Desktop/Generated-Digits/")
    destination_path.mkdir(parents=True, exist_ok=True)

    while True:
        try:
            num_threads = int(input("Enter the number of threads: "))
            if num_threads <= 0:
                raise ValueError("Number of threads must be a positive integer.")
        except ValueError:
            print("Invalid input. Number of threads must be a positive integer.")
        else:
            break

    print("Select the type of generation:")
    print("1. Generate random digits")
    print("2. Generate random passwords")
    print("3. Generate random words")
    print("4. Generate all")

    while True:
        try:
            generation_type = int(input("Enter the generation type (1/2/3/4): "))
            if generation_type not in [GENERATE_RANDOM_DIGITS, GENERATE_RANDOM_PASSWORDS, GENERATE_RANDOM_WORDS, GENERATE_ALL]:
                raise ValueError("Invalid input. Please enter 1, 2, 3, or 4.")
        except ValueError as e:
            print(e)
        else:
            break

    if generation_type == GENERATE_ALL:
        generation_types = [GENERATE_RANDOM_DIGITS, GENERATE_RANDOM_PASSWORDS, GENERATE_RANDOM_WORDS]
    else:
        generation_types = [generation_type]

    sizes = [4, 6, 8, 16]

    while True:
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for size in sizes:
                for gen_type in generation_types:
                    futures.append(executor.submit(generate_and_save, size, destination_path, gen_type))
            futures.append(executor.submit(check_existing_codes_in_thread, destination_path, generation_type, num_threads // 5))

            concurrent.futures.wait(futures)

        print("Waiting for the next round of generation...")
        time.sleep(0)

if __name__ == "__main__":
    main()
