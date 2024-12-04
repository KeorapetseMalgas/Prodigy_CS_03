import string

def check_password_strength(password):
    # Password checks
    upper_case = any(c in string.ascii_uppercase for c in password)
    lower_case = any(c in string.ascii_lowercase for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c in string.digits for c in password)
    length_score = len(password) >= 8  # Minimum length of 8

    total_rate = sum([upper_case, lower_case, special, digits, length_score])
    
    # Debugging: Show the individual results
    print(f"Debug - Password: {password}")
    print(f"Uppercase: {upper_case}, Lowercase: {lower_case}, Special: {special}, Digits: {digits}, Length >= 8: {length_score}")
    print(f"Total rate: {total_rate}")
    
    return total_rate

def is_common_password(password, file_path=r"C:\Users\malga\OneDrive\Documents\commonpasswords.txt.txt"):
    try:
        # Open the file and read its contents
        with open(file_path, "r") as file:
            common_passwords = file.read().splitlines()  # Read lines and remove newline characters

        # Check if the password is in the common passwords list
        if password in common_passwords:
            return True
        else:
            return False
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return False

# Ask for password and check the complexity until it's strong enough
while True:
    password = input("Enter your password: ")

    # Check if the password is in the common password list
    if is_common_password(password):
        print("Password is too common and may have been leaked! Try another one.")
        continue  # Prompt the user to enter a new password

    total_rate = check_password_strength(password)

    # Give feedback based on total_rate
    if total_rate == 5:
        print("Very strong password!")
        break  # Exit the loop if password is strong enough
    elif total_rate == 4:
        print("Good password, but you can improve it further!")
    elif total_rate == 3:
        print("Weak password, try including more types of characters.")
    elif total_rate == 2:
        print("Very weak password. Try adding uppercase, lowercase, digits, and special characters.")
    else:
        print("Password is extremely weak. Please improve it!")


