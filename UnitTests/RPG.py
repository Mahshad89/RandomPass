import random
import string
import math
import secrets

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True, pronounceable=False, entropy=None):
    if pronounceable:
        return generate_pronounceable_password(length)
    
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if entropy:
        min_length = math.ceil(entropy / math.log2(len(characters)))
        if length < min_length:
            raise ValueError(f"Password length must be at least {min_length} for the specified entropy")

    password = [secrets.choice(characters) for _ in range(length)]
    return ''.join(password)

def generate_pronounceable_password(length):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    password = ''

    for i in range(length):
        if i % 2 == 0:
            password += random.choice(consonants)
        else:
            password += random.choice(vowels)

    return password

def check_password_strength(password):
    upper_case_letters = any(char.isupper() for char in password)
    lower_case_letters = any(char.islower() for char in password)
    has_digits = any(char.isdigit() for char in password)
    special_characters = any(char in string.punctuation for char in password)
    
    score = 0
    if upper_case_letters:
        score += 1
    if lower_case_letters:
        score += 1
    if has_digits:
        score += 1
    if special_characters:
        score += 1
    
    return score

def generate_passphrase(word_list, num_words=4, delimiter=' '):
    passphrase = [random.choice(word_list) for _ in range(num_words)]
    return delimiter.join(passphrase)

def save_passwords_to_file(passwords, filename="passwords.txt"):
    with open(filename, "a") as file:
        for password in passwords:
            file.write(password + "\n")

def main():
    word_list = ["apple", "banana", "cherry", "dog", "elephant", "flower", "giraffe", "honey", "ice", "jungle"]
    
    while True:
        print("Password Generator")
        print("1. Generate Random Password")
        print("2. Generate Passphrase")
        choice = int(input("Choose an option (1/2): "))
        
        if choice == 1:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            length = int(input("Enter the length of the password: "))
            use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
            use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
            use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
            entropy = float(input("Specify password entropy (optional): ") or 0)
            
            passwords = []
            for _ in range(num_passwords):
                try:
                    password = generate_password(length, use_upper, use_digits, use_special, entropy=entropy)
                    passwords.append(password)
                    print(f"Generated Password: {password}")
                    strength = check_password_strength(password)
                    print(f"Password Strength: {strength}/4")
                except ValueError as e:
                    print(f"Error: {e}")

            save_to_file = input("Save passwords to a file? (y/n): ").strip().lower()
            if save_to_file == 'y':
                save_passwords_to_file(passwords)
                print(f"Passwords saved to 'passwords.txt")

        elif choice == 2:
            num_passphrases = int(input("Enter the number of passphrases to generate: "))
            num_words = int(input("Enter the number of words per passphrase: "))
            delimiter = input("Enter the word delimiter (default is space): ")
            delimiter = delimiter if delimiter else ' '
            
            passphrases = [generate_passphrase(word_list, num_words, delimiter) for _ in range(num_passphrases)]
            for passphrase in passphrases:
                print(f"Generated Passphrase: {passphrase}")

        another = input("Generate more passwords/passphrases? (y/n): ").strip().lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()


