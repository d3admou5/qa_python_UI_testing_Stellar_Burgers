# Sprint_4
## UI-тесты для сайта Stellar Burgers

## Описание
Набор автотестов на Python с использованием `Selenium` и `Pytest` для проверки ключевых сценариев UI сайта [stellarburgers.nomoreparties.site](https://stellarburgers.nomoreparties.site).

---

## Покрытие

###  Регистрация
-  Успешная регистрация с валидными данными — `test_successful_registration`
-  Ошибка при вводе короткого пароля — `test_short_password_error`

###  Вход (Login)
-  Вход через кнопку «Войти в аккаунт» на главной — `test_login_from_main_page`
-  Вход через кнопку «Личный кабинет» — `test_login_from_personal_account_button`
-  Вход через ссылку из формы регистрации — `test_login_from_register_page`
-  Вход через ссылку из формы восстановления пароля — `test_login_from_forgot_password_page`

### Выход (Logout)
-  Успешный выход из аккаунта — `test_logout_from_profile`

###  Личный кабинет
-  Переход по кнопке «Личный кабинет» — `test_go_to_personal_account`
-  Переход из профиля в конструктор по кнопке — `test_go_from_profile_to_constructor`
-  Переход из профиля в конструктор по клику на логотип — `test_go_to_constructor_by_logo`

###  Конструктор
-  Переключение между вкладками: «Булки», «Соусы», «Начинки» — `test_constructor_tab_switch`

---

##  Запуск

Установи зависимости:

```bash
  pip install -r requirements.txt
```

## Структура проекта
```
.
├── tests/                   # UI-тесты
│   ├── test_register.py  
│   ├── test_login.py    
│   ├── test_logout.py     
│   ├── test_profile.py 
│   └── test_constructor_tabs.py
├── helper/ 
│   ├── constructor.py       # Функция для клика по вкладке и ожидания её активации
│   ├── registration.py      # Функция для заполнения формы регистрациии
│   └── user_generator.py    # Генерация случайных пользователей
├── locators.py              # Локаторы страниц
├── data.py                  # Данные: логин/пароль и др.
├── conftest.py              # Фикстуры и общие настройки
├── urls.py                  # Все URL'ы проекта (используется BASE_URL)
├── requirements.txt         # Зависимости проекта
└── README.md                # Документация проекта

```
