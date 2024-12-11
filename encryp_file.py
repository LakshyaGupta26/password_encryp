from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_password(password):
    f = Fernet(load_key())
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password):
    f = Fernet(load_key())
    return f.decrypt(encrypted_password).decode()
