def is_valid_password(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_characters = "$#@"
    
    if len(password) < 6:
        return False
    
    for char in password:
        if 'a' <= char <= 'z':
            has_lower = True
        elif 'A' <= char <= 'Z':
            has_upper = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    return has_lower and has_upper and has_digit and has_special

def main():
    password = input("Enter a password: ")
    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid.")

# Example usage
main()