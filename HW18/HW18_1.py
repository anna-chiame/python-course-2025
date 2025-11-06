# Task 1

class User :
    """
       Клас User реалізує перевірку (валідацію) електронної адреси (email)
       під час створення нового об’єкта користувача.

       Основна мета — перевірити коректність email за рядом умов:
       - тип даних (повинен бути рядком)
       - відсутність пробілів
       - правильне розташування символів '.' і '@'
       - відсутність заборонених символів
       - наявність доменного імені після '@'

       Використовує класовий метод validate() для виконання перевірок.
       """

    def __init__(self, email):
        """
               Ініціалізація нового користувача з email.

               :param email: str - електронна адреса користувача.
               :raises TypeError: якщо email не є рядком.
               :raises ValueError: якщо email не відповідає правилам формату.
               """
        self.validate(email)
        self.email = email

    @classmethod
    def validate (cls, email) :
        """
               Валідатор електронної адреси користувача.

               Метод перевіряє, чи email має коректну структуру:
               - є рядком без пробілів
               - містить тільки латинські літери, цифри, '.' та '@'
               - має рівно один '@' і коректне доменне ім’я після нього
               - не починається та не закінчується символами '.' або '@'
               - не містить заборонених символів із списку INVALID_CHARS

               :param email: str - електронна адреса для перевірки.
               :return: bool - True, якщо email валідний.
               :raises TypeError: якщо email не є рядком.
               :raises ValueError: якщо порушено будь-яке з правил форматування.
               """
        INVALID_CHARS = """",:;()[]\\/<>?"\'!*&#^%=|"""
        # перевірка на тип
        if not isinstance(email, str):
            raise TypeError("Email має бути рядком")
        # видаляємо пробіли по краях
        email = email.strip()
        # якщо имейл пустий
        if email == "" :
            raise ValueError ("Email не може бути порожнім")
        # якщо у Email є пробіли
        if " " in  email :
            raise ValueError ("Email не може містити пробіли")
        # перевіряємо, щоб email не починався і не закінчувався крапками
        if email.startswith(".") :
            raise ValueError ("Email не може починатися з крапки")
        if email.endswith(".") :
            raise ValueError ("Email не може закінчуватися крапкою")
        #якщо починається чи закінчується @
        if email.startswith("@") :
            raise ValueError ("Email не може починатися з @")
        if email.endswith("@") :
            raise ValueError ("Email не може закінчуватися @")
        # перевіряємо щоб не було двох крапок підряд
        if ".." in email :
            raise ValueError ("""Email не може містити ".." """)
        # якщо є заборонені символи INVALID_CHARS
        for char in  INVALID_CHARS :
            if char in email:
                raise ValueError (f"Email містить заборонений символ: {char}")
        # якщо відсутня @
        if email.count("@") == 0 :
            raise ValueError ("Email має містити @ - наприклад example@domen.com ")
        # якщо більше 1 @ і ділимо на префікс і доменне ім'я
        parts = email.split ("@")
        if len(parts) != 2 :
            raise ValueError ("Email має містити тільки 1 @")
        prefix, domen = parts
        # якщо частини пусті
        if prefix =="" :
            raise ValueError ("Порожня частина до @")
        if domen == "" :
            raise ValueError("Email має містити дані домену після @")
        #перевірка на латинські літери
        for char in prefix :
            if not ("a" <= char.lower() <= "z" or char.isdigit()) :
                raise ValueError ("Email має містити тільки латинські літери")
        for char in domen :
            if not ("a" <= char.lower() <= "z" or char.isdigit() or char == ".") :
                raise ValueError ("Email має містити тільки латинські літери")
        #перевірка домену на присутність крапки, її місце
        if domen.startswith(".") :
            raise ValueError ("Крапка в доменному імені не на свому місці")
        if "." not in domen :
            raise ValueError("Доменне і`мя після @ має містити крапку")
        return True

 # Приклад для перевірки
try:
    user1 = User("anna@gmail.com")
    print("Успіх :", user1.email)

    user2 = User("bad email@domain")
except Exception as e:
    print("Помилка :", e)















