from selenium.webdriver.common.by import By

# === Главная страница ===
class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
# Ниже используются для переходов в конструктор (в т.ч. из личного кабинета)
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор" в хедере
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Клик по логотипу Stellar Burgers

# === Страница регистрации ===
class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение об ошибке

# === Страница входа ===
class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")  # Поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # Поле пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")  # Ссылка на регистрацию
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка на восстановление пароля

# === Страница восстановления пароля ===
class ProfilePageLocators:
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выйти"

# === Конструктор (разделы) ===
class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Вкладка "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Вкладка "Начинки"
