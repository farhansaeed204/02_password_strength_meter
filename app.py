import re
import streamlit as st
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    common_words = ["password", "123456", "qwerty", "admin", "letmein"]
    if any(word in password.lower() for word in common_words):
        feedback.append("Avoid using common words or sequences in your password.")
    
   
    if re.search(r'(.)\1{2,}', password):
        feedback.append("Avoid using consecutive repeated characters.")
  
    if re.search(r'123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz', password.lower()):
        feedback.append("Avoid using sequential characters (e.g., '1234', 'abcd').")
    

    if score >= 4 and len(set(password)) >= 6:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return strength, feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

def main():
    st.title("🔐 Password Strength Meter")
    st.write("Enter a password to check its strength and get suggestions for improvement.")
    password = st.text_input("Enter a password:", type="password")
    
    if st.button("Check Strength"):
        strength, feedback = check_password_strength(password)
        st.subheader(f"Password Strength: {strength}")
        
        if feedback:
            st.warning("Suggestions to improve:")
            for tip in feedback:
                st.write(f"- {tip}")
        else:
            st.success("Great job! Your password is strong.")
    
    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password()
        st.text_input("Suggested Strong Password:", strong_password)
    
    st.write("🔹 Tip: Use a combination of uppercase, lowercase, numbers, and special characters for a strong password.")

if __name__ == "__main__":
    main()
