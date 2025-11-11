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

user_str = input("Введіть рядок: ")

stack = Stack()
# додаємо посимвольно в стек
for ch in user_str:
    stack.push(ch)
# змінна зворотнього порядку
reversed_user_str = ""
# витягуємо символи в зворотньому порядку
for _ in range(len(user_str)):
    reversed_user_str += stack.pop()

print("Рядок у зворотному порядку:", reversed_user_str)

