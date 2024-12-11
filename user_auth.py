from bcrypt import hashpw, gensalt, checkpw

def hash_password(password):
    return hashpw(password.encode(), gensalt())

def check_password(hashed, user_password):
    return checkpw(user_password.encode(), hashed)
