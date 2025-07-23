from faker import Faker

faker = Faker()

def generate_registration_data(password_length=12):
    name = faker.first_name()
    email = faker.email()
    password = faker.password(
        length=password_length,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )
    return name, email, password
