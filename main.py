import os
import time
import random
import shutil


def text_to_binary(text):
    binary_text = ""
    for char in text:
        ascii_code = ord(char)
        binary_char = format(ascii_code, "08b")
        binary_text += binary_char + " "
    return binary_text


def binary_to_text(binary_text):
    text = ""
    binary_chars = binary_text.split()
    for binary_char in binary_chars:
        decimal_code = int(binary_char, 2)
        character = chr(decimal_code)
        text += character
    return text


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_slow(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()


def generate_matrix_effect():
    columns, rows = shutil.get_terminal_size()
    binary_digits = ["0", "1"]
    update_interval = 0.1
    positions = [0] * columns

    try:
        while True:
            clear_screen()
            for i in range(columns):
                if random.random() > 0.5:
                    positions[i] = 0
                if positions[i] < rows:
                    char = random.choice(binary_digits)
                    print(f"\033[{positions[i]};{i}H{char}", end="", flush=True)
                    positions[i] += 1
            time.sleep(update_interval)
    except KeyboardInterrupt:
        clear_screen()
        print("Matrix effect terminated.")


while True:
    clear_screen()
    choice = input(
        "What do you want to do?\n1. Translate text to binary\n2. Translate binary to text\n3. Matrix effect\n4. Exit\nChoose an option: "
    )

    if choice == "1":
        input_text = input("Enter text to translate to binary: ")
        binary_representation = text_to_binary(input_text)
        print_slow("\nTranslated into binary:\n")
        print_slow(binary_representation)
    elif choice == "2":
        binary_input = input("Enter binary to translate to text: ")
        text_representation = binary_to_text(binary_input)
        print_slow("\nTranslated into text:\n")
        print_slow(text_representation)
    elif choice == "3":
        generate_matrix_effect()
    elif choice == "4":
        print("Closing the application...")
        break
    else:
        print("Incorrect selection. Try again.")

    input("\nPress Enter to continue...")
