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

def is_balanced (example_data: str) ->bool :
        # пари для балансу
    pairs = {"(": ")", "{" : "}", "[" : "]"}
        #пустий список куди ми будемо класти наш ключ-відкриваючу дужку
    stack = Stack()

    # перебираємо кожен символ рядка
    for ch in example_data :
        # якщо символ один із ключів, то додаємо в стак для порівняння значення
        if ch in pairs :
            stack.push(ch)
        # перевіряємо закриваючу дужку
        elif ch in pairs.values():
            # якщо стак порожній то там немає відкриваючої дужки
            if  stack.is_empty():
                return False
            # Вилучаємо зі стаку останню(верхню) відкриваючу по принципу LIFO і вона стає ключем
            top = stack.pop()
            # Порівняння чи відповідає ключу pairs[top] те значення яке ми зараз бачимо перед собою ch
            if ch != pairs[top]:
                return False
    # якщо стек порожній то всі значення збалансовані
    return stack.is_empty()

print(is_balanced('({[()]}}'))





