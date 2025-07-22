from selenium.webdriver.common.by import By

# Главная страница
class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
# Ниже используются для переходов в конструктор (в т.ч. из личного кабинета)
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Кнопка "Конструктор" в хедере
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Клик по логотипу Stellar Burgers

# Страница регистрации
class RegistrationLocators:
    NAME_INPUT = (By.XPATH, "//div[label[text()='Имя']]/input")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//div[label[text()='Пароль']]/input")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    ERROR_HINT = (By.XPATH, "//p[text()='Некорректный пароль']")  # Сообщение об ошибке (например, при коротком пароле. Нужно ввести не валидный пароль)

# Страница входа
class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input") # Поле email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")  # Поле пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")  # Ссылка на регистрацию
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка на восстановление пароля

# Страница восстановления пароля
class RegisterPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")  # Ссылка "Войти" под формами

# Кнопка Выход логаут
class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# Конструктор (разделы)
class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span")
