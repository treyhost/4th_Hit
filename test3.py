import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 12  # Change this to set the desired length of the password
    random_password = generate_random_password(password_length)
    print("Your unique random password is:", random_password)
