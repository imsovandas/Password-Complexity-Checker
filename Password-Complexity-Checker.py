import re

def check_password_strength(password):
    # Minimum length is 8 characters
    if len(password) < 8:
        return "Your Password is Very Weak: Password should be at least 8 characters long. \n "

    # Check for both uppercase and lowercase letters
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return "Your Password is Very Weak: Password should contain a mix of uppercase and lowercase letters. \n "
        
    # Check for at least one digit
    if not any(c.isdigit() for c in password):
        return "Your Password is Weak: Password should contain at least one digit. \n "
     
    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Your Password is Weak: Password should contain at least one special character. \n "
    
    # Check for consecutive characters (e.g., "abc", "123")
    if re.search(r"(abc|123|xyz)", password, re.IGNORECASE):
        return "Your Password is moderate: Avoid using common consecutive character sequences. \n "

    # Check for repeated characters (e.g., "aa", "111")
    if re.search(r"(.)\1", password):
        return "Your Password is moderate: Avoid using repeated characters. \n "
    # Strong password
    return "Your password is very strong; it meets all the criteria. \n "

# Example usage
print("\n--------------------------------------")
print("Password Complexity Checker By Sovan Das")
print("--------------------------------------\n")
password_input = input("Enter your password: ")
print(" ")
result = check_password_strength(password_input)
print(result)