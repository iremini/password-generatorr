
import random
import string

def generate_password(length=12):
    """
    Generate a random password with a given length.
    Default length is 12 characters.
    """
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    # All possible characters: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (default is 12): "))
    except ValueError:
        length = 12  # Default length if user input is invalid
    
    password = generate_password(length)
    if password:
        print(f"Your generated password is: {password}")
