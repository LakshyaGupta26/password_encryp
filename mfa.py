import pyotp

def generate_secret_key():
    return pyotp.random_base32()

def get_otp(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()

def validate_otp(secret_key, user_otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(user_otp)
