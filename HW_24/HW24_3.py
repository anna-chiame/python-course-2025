class Stack:
    def __init__(self):
        self.items = []

    # додаємо
    def push(self, item):
        self.items.append(item)
    # витягуємо останній і видаємо його
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise ValueError("Стек порожній")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # новий метод
    def get_from_stack(self, e):
        """
        Шукає та повертає елемент 'e' зі стека, зберігаючи порядок інших елементів.
        Використовує допоміжний стек.
        """
        add_stack = Stack()
        found_element = None

        # 1. Пошук елемента і переміщення інших в add_stack
        while not self.is_empty():
            current = self.pop()
            # Знайшли елемент, припиняємо пошук
            if current == e:
                found_element = current
                break
            else:
                add_stack.push(current)

        # 2. Відновлення порядку: повертаємо елементи з add_stack назад

        while not add_stack.is_empty():
            self.push(add_stack.pop())

        # 3. Перевірка результату
        if found_element is None:
            raise ValueError(f"Елемент '{e}' не знайдено у стеку.")

        return found_element