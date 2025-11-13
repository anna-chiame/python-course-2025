#2
class Node:
    def __init__(self, data):
        # зберігає дані вузла
        self.data = data
        # вказівник на наступний вузол
        self.next = None
class Stack:
    def __init__(self):
        # голова списку, яка представляє "верхівку" стека
        self.head = None
        self.size = 0  #  розмір

    # перевірка Порожнечі
    def is_empty(self):
        return self.head is None

    # розмір
    def get_size(self):
        return self.size

    # додаємо елемент на верхівку стека
    def push(self, data):
        new_node = Node(data)
        # новий вузол вказує на поточну голову
        new_node.next = self.head
        # новий вузол стає новою головою, верхівкою стеку
        self.head = new_node
        self.size += 1
        print(f"PUSH: Додано {data}")

    # видаляємо та повертаємо елемент з верхівки стека
    def pop(self):
        # перевірка, чи стек не порожній
        if self.is_empty():
            print("POP: Стек порожній. Неможливо видалити.")
            return None
        # зберігаємо дані поточної голови для повернення
        popped_data = self.head.data
        # переміщуємо голову на наступний вузол
        self.head = self.head.next
        self.size -= 1
        print(f"POP: Видалено {popped_data}")
        return popped_data

    # повертає елемент з верхівки без його видалення
    def peek(self):
        if self.is_empty():
            return "Стек порожній"
        return self.head.data


# Робота

my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print(f"PEEK: Верхівка стека: {my_stack.peek()}")

my_stack.pop()
my_stack.pop()
print(f"Розмір стека: {my_stack.get_size()}")


