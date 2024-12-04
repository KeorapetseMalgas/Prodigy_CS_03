import string

def check_password_strength(password):
    
    upper_case = any(c in string.ascii_uppercase for c in password)
    lower_case = any(c in string.ascii_lowercase for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c in string.digits for c in password)
    length_score = len(password) >= 8  

    total_rate = sum([upper_case, lower_case, special, digits, length_score])
    
    
    print(f"Debug - Password: {password}")
    print(f"Uppercase: {upper_case}, Lowercase: {lower_case}, Special: {special}, Digits: {digits}, Length >= 8: {length_score}")
    print(f"Total rate: {total_rate}")
    
    return total_rate

def is_common_password(password, file_path=r"C:\Users\malga\OneDrive\Documents\commonpasswords.txt.txt"):
    try:
        
        with open(file_path, "r") as file:
            common_passwords = file.read().splitlines()  

        
        if password in common_passwords:
            return True
        else:
            return False
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return False


while True:
    password = input("Enter your password: ")

    
    if is_common_password(password):
        print("Password is too common and may have been leaked! Try another one.")
        continue  

    total_rate = check_password_strength(password)

    
    if total_rate == 5:
        print("Very strong password!")
        break  
    elif total_rate == 4:
        print("Good password, but you can improve it further!")
    elif total_rate == 3:
        print("Weak password, try including more types of characters.")
    elif total_rate == 2:
        print("Very weak password. Try adding uppercase, lowercase, digits, and special characters.")
    else:
        print("Password is extremely weak. Please improve it!")


