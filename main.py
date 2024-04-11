import os
import time


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
        time.sleep(0.1)
    print()


while True:
    clear_screen()
    choice = input(
        "What do you want to do?\n1. Translate text to binary\n2. Translate binary to text\n3. Exit\nChoose an option: "
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
        print("Closing the application...")
        break
    else:
        print("Incorrect selection. Try again.")

    input("\nPress Enter to continue...")
