import random
from helper import ask

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"

characters = LOWERCASE
password = ""

while True:
    try:
        length = int(input("Enter password length: "))
        if length > 0:
            break
        print("Length must be greater than 0.")
    except ValueError:
        print("Enter a valid number!")


if ask("Include numbers? (y/n): ") == "y":
    characters += NUMBERS

if ask("Include uppercase? (y/n): ") == "y":
    characters += UPPERCASE

if ask("Include symbols? (y/n): ") == "y":
    characters += SYMBOLS


for _ in range(length):
    password += random.choice(characters)

print(f'Generated password: {password}')
