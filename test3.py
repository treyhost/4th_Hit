import random
import string

# List of character names from "The Matrix"
matrix_characters = [
    "Neo",
    "Morpheus",
    "Trinity",
    "Agent Smith",
    "Cypher",
    "The Oracle",
    "The Architect"
]

def generate_random_password(length, character_name):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length - len(character_name)))
    password += character_name
    return password

if __name__ == "__main__":
    password_length = 17  # Change this to set the desired length of the password (length of name + additional characters)
    random_character_name = random.choice(matrix_characters)
    random_password = generate_random_password(password_length, random_character_name)
    print("Your unique random password with a 'Matrix' character name is:", random_password)
