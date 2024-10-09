class Locators:
    # Регистрация
    REGISTER_NAME_FIELD = "input[name='name']"  # Поле «Имя» в форме регистрации
    REGISTER_EMAIL_FIELD = "input[name='email']"  # Поле «Email» в форме регистрации
    REGISTER_PASSWORD_FIELD = "input[name='Пароль']"  # Поле «Пароль» в форме регистрации
    REGISTER_BUTTON = "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa"  # Кнопка «Зарегистрироваться» в форме регистрации
    REGISTER_LINK = "a.Auth_link__1fOlj[href='/register']"  # Ссылка «Зарегистрироваться» в форме входа

    # Вход
    LOGIN_EMAIL_FIELD = "input[name='name']"  # Поле «Email» в форме входа
    LOGIN_PASSWORD_FIELD = "input[name='Пароль']"  # Поле «Пароль» в форме входа
    LOGIN_BUTTON = "a.Auth_link__1fOlj[href='/login']"  # Кнопка "Войти" в форме регистрации
    LOGIN_LINK = "a.Auth_link__1fOlj[href='/login']"  # Кнопка «Войти» на странице восстановления пароля

    # Личный кабинет
    PERSONAL_ACCOUNT_BUTTON = "p.AppHeader_header__linkText__3q_va.ml-2" # Кнопка «Личный кабинет» на главной странице

    # Восстановление пароля
    RECOVERY_PASSWORD_LINK = "a.Auth_link__1fOlj[href='/forgot-password']"  # Ссылка «Восстановить пароль» на странице входа

    # Войти в аккаунт на главной странице
    MAIN_LOGIN_BUTTON = "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg"  # Кнопка «Войти в аккаунт» на главной странице

    # Логотип
    LOGO_BUTTON = "//*[@id='root']/div/header/nav/div/a/svg"  # Логотип Stellar Burgers

    # Выход
    LOGOUT_BUTTON = "button.Account_button__14Yp3"  # Кнопка «Выйти» в личном кабинете

    # Разделы конструктора
    CONSTRUCTOR_BUNS = "//span[text()='Булки']"  # Раздел «Булки» на главной странице
    CONSTRUCTOR_SAUCES = "//span[text()='Соусы']"  # Раздел «Соусы» на главной странице
    CONSTRUCTOR_FILLINGS = "//span[text()='Начинки']"  # Раздел «Начинки» на главной странице

