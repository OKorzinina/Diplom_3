from faker import Faker


fake = Faker('ru_RU')


class UserGenerator:
    @staticmethod
    def generate_user():
        return {
            'name': fake.first_name(),
            'email': fake.email(),
            'password': fake.password(length=10)
        }
    
    @staticmethod
    def generate_invalid_email():
        return "invalid-email"
    
    @staticmethod
    def generate_short_password():
        return "123"
