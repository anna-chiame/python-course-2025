#Task 2


class Boss :
    """
        Клас Boss

        Кожен бос має:
          - унікальний ідентифікатор (id)
          - ім’я (name)
          - компанію, у якій працює (company)
          - список своїх працівників (_workers)

        Цей клас дозволяє переглядати список працівників та додавати нових.
        """

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        #  приватний список працівників
        self._workers = []

    @property
    def workers(self):
        """Getter: Повертає список працівників поточного боса.

        :return: list, список об’єктів класу Worker.
        """
        return self._workers

    def add_worker (self, worker) :
        """
        Додає працівника до списку поточного боса.

        :param worker: Worker, екземпляр класу Worker.
        :raises ValueError: якщо переданий об’єкт не є екземпляром Worker.
        """
        # Перевірка типу
        if not isinstance(worker, Worker) :
            raise ValueError("Можна додавати лише об’єкти класу Worker.")
        # Якщо цього працівника ще немає в списку додаємо
        if worker  not in self._workers :
            self._workers.append(worker)

    def __repr__(self):
        """Повертає  текстове представлення об’єкта."""
        return f"Boss({self.name}, {self.company})"


class Worker:
    """
        Клас Worker

        Кожен працівник має:
          - унікальний ідентифікатор (id)
          - ім’я (name)
          - компанію (company)
          - посилання на свого боса (boss)

        Під час створення об’єкта відбувається автоматичне встановлення зв’язку
        між працівником і босом."""

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        #  викликає setter, створює зв’язок
        self.boss = boss

    @property
    def boss(self):
        """Getter: Повертає поточного боса працівника.

        :return: Boss, екземпляр класу Boss.
        """
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        """Setter: Оновлює боса для працівника з перевіркою типу та синхронізацією списків.

        :param new_boss: Boss — новий бос.
        :raises ValueError: якщо передане значення не є об’єктом класу Boss."""

        # Перевірка типу
        if not isinstance(new_boss, Boss):
            raise ValueError("Бос має бути екземпляром класу Boss.")
        # Якщо працівник вже має боса то прибираємо його зі старого списку
        if self._boss and self in self._boss.workers:
            self._boss.workers.remove(self)
        # Оновлюємо поле з новим босом
        self._boss = new_boss
        # Якщо цього працівника ще немає у списку нового боса то  додаємо
        if self not in new_boss.workers:
            new_boss.add_worker(self)

    def __repr__(self):
        """Повертає зручне текстове представлення об’єкта."""
        boss_name = self._boss.name if self._boss else "No boss"
        return f"Worker({self.name}, boss : {self._boss.name})"

# Приклади для перевірки

boss_1 = Boss(1, "Олег", "Google")
boss_2 = Boss(2, "Ірина", "Apple")
boss_3 = Boss(3, "Петро", "Amazon")

worker_1 = Worker(101, "Анна", "Google", boss_1)
worker_2 = Worker(102, "Марк", "Google", boss_1)
worker_3 = Worker(103, "Юлія", "Apple", boss_2)
worker_4 = Worker(104, "Дмитро", "Amazon", boss_3)
worker_5 = Worker(105, "Катерина", "Google", boss_1)
print ("-"*20)
print("Працівники Боса_1 :", boss_1.workers)
print("Працівники Боса_2:", boss_2.workers)
print("Працівники Боса_3:", boss_3.workers)
print ("-"*20)
worker_1.boss = boss_2
print("Працівники Боса_2:", boss_2.workers)
print ("-"*20)
boss_3.add_worker(worker_5)
print("Працівники Боса_3:", boss_3.workers)