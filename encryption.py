import os 
import time
import string

def clear_screen():
    os.system("cls" if os.name == "nt" else 'clear')

user_message = input("\nEnter your word or sentence: ")
alphabets = string.ascii_lowercase
encrypted_message = ""

while True:
    shift_number = input("\nEnter a number: ")

    if shift_number.isdigit():
        break
    else:
        print("\nThat's not a number or integer\n")
        time.sleep(1)
        print("Please try again...")
        time.sleep(2)
        clear_screen()
        continue

for letter in user_message:
    if letter.lower() in alphabets:
        original_position = alphabets.index(letter.lower())
        new_position = (original_position + int(shift_number)) % len(alphabets)
        encrypted_letter = alphabets[new_position]
        
        if letter.isupper():
            encrypted_message += encrypted_letter.upper()
        else:
            encrypted_message += encrypted_letter

    else:
        encrypted_message += letter

print(f"\n\nThe original message: {user_message}\n\n")
print(f"The encrypted message: {encrypted_message}")
            












