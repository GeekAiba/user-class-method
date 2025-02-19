from datetime import date

class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = None
        self.password = None

    def get_details(self):
        details = (
            f"User ID: {self.user_id}\n"
            f"Name: {self.name}\n"
            f"Surname: {self.surname}\n"
            f"Email: {self.email}\n"
            f"Password: {'*' * len(self.password) if self.password else 'None'}\n"
            f"Birthday: {self.birthday.strftime('%Y-%m-%d')}\n"
            f"Age: {self.get_age()}"
        )
        return details

    def get_age(self):
        today = date.today()
        birth_date = self.birthday
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age