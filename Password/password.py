import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the password length: "))
        if password_length <= 0:
            print("Error: Password length must be a positive integer.")
            return
    except ValueError:
        print("Error: Please enter a valid integer for password length.")
        return

    generated_password = generate_password(password_length)

    print(f"\nGenerated Password: {generated_password}")

    print("\nPrinted Password:")
    print(generated_password)

if __name__ == "__main__":
    main()
