class Shaxs:
    def __init(self, name, surname, passport, b_year):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.b_year = b_year

    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"Passport: {self.passport}, {self.b_year}-yilda tug'ilgan."
        return info

    def get_age(self, year):
        return year - self.b_year
