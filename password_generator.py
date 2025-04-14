# Secure Vault Key Generator
import string
import secrets

def generate_secure_key():
    print("🔒 Welcome to Fort Knox Password Generator 🔒")
    key_length = int(input("Enter desired security key length (8-64 recommended): "))
    
    alphabet_chars = string.ascii_letters
    numeric_chars = string.digits
    special_chars = string.punctuation
    character_pool = alphabet_chars + numeric_chars + special_chars
    
    security_key = "".join(secrets.choice(character_pool) for _ in range(key_length))
    
    print("\n⚡ Your ultra-secure access key:")
    print(f"🔑 {security_key}")
    print("\n⚠️ Remember to store this securely and never share it!")

generate_secure_key()
