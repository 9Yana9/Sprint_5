from selenium.webdriver.common.by import By


class Locators:
    # Регистрация
    REGISTER_NAME_FIELD = By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input[@type='text']"  # Поле «Имя» в форме регистрации
    REGISTER_EMAIL_FIELD = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input[@type='text']")# Поле «Email» в форме регистрации
    REGISTER_PASSWORD_FIELD = (By.XPATH, "//input[@type='password' and @name='Пароль']")  # Поле «Пароль» в форме регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")    # Кнопка «Зарегистрироваться» в форме регистрации

    # Вход
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input[@type='text']")  # Поле «Email» в форме входа
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input[@type='password']")  # Поле «Пароль» в форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")    # Кнопка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")  # Кнопка «Войти» на странице регистрации
    LOGIN_LINK_2 = (By.XPATH, "//a[contains(text(), 'Войти')]") # Кнопка «Войти» на странице восстановления пароля
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"

    # Личный кабинет
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") # Кнопка «Личный кабинет» на главной странице
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]") #Кнопка "Личный кабинет" после входа

    # Логотип
    LOGO_BUTTON = (By.XPATH, "//a[@href='/' and contains(., '')]") # Логотип Stellar Burgers

    # Выход
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")  # Кнопка «Выйти» в личном кабинете

    # Разделы конструктора
    CONSTRUCTOR_BUNS = (By.XPATH, "//span[contains(text(), 'Начинки')]")  # Раздел «Булки» на главной странице
    CONSTRUCTOR_SAUCES = (By.XPATH, "//span[contains(text(), 'Соусы')]")  # Раздел «Соусы» на главной странице
    CONSTRUCTOR_FILLINGS = (By.XPATH, "//span[contains(text(), 'Начинки')]")  # Раздел «Начинки» на главной странице
    CONSTRUCTOR_BUTTON =  (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Конструктор')]")
