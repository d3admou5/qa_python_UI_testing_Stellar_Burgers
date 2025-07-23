from locators import RegistrationLocators

# Функция для заполнения формы регистрации
def fill_registration_form(driver, name, email, password):
    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()


# Вынес функцию fill_registration_form в отдельный файл helpers/registration_form.py.
# В рамках проекта у нас один тест, который использует эту функцию два раза.