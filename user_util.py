import random
from datetime import datetime
import string
import re

class UserUtil:
    @staticmethod
    def generate_user_id():
        year_part = datetime.now().strftime("%y")
        random_part = ''.join(str(random.randint(0, 9)) for _ in range(7))
        return f"{year_part}{random_part}"

    @staticmethod
    def generate_password():
        uppercase = random.choice(string.ascii_uppercase)
        lowercase = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        special = random.choice(string.punctuation)
        all_chars = string.ascii_letters + string.digits + string.punctuation
        remaining = [random.choice(all_chars) for _ in range(4)]
        password_chars = [uppercase, lowercase, digit, special] + remaining
        random.shuffle(password_chars)
        password = ''.join(password_chars)
        while len(password) < 8:
            password += random.choice(all_chars)
        return password

    @staticmethod
    def is_strong_password(password):
        if len(password) < 8:
            return False
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        return has_upper and has_lower and has_digit and has_special

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r'^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$'
        return re.match(pattern, email) is not None