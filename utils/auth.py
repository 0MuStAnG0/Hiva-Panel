import random

OTP_STORAGE = {}

def generate_otp(user_id):
    code = random.randint(100000, 999999)
    OTP_STORAGE[user_id] = code
    return code

def verify_otp(user_id, code):
    return OTP_STORAGE.get(user_id) == int(code)
