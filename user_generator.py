from faker import Faker

faker = Faker()

def generate_registration_data():
    # Генерация данных для успешной регистрации:
    # - name: любое имя
    # - email: случайная почта
    # - password: валидный (12 символов, содержит буквы, цифры, спецсимволы и заглавные буквы)
    name = faker.first_name()
    email = faker.email()
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password

def generate_registration_data_invalid_password():
    # Генерация данных с невалидным паролем:
    # - пароль слишком короткий (5 символов), не проходит проверку (должен быть 6+)
    name = faker.first_name()
    email = faker.email()
    password = faker.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password
