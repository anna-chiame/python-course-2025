# 3

class Node:
    def __init__(self, data):
        # зберігає дані вузла
        self.data = data
        # вказівник на наступний вузол
        self.next = None

class Queue:
    def __init__(self):
        # голова : елемент, який буде видалено наступним (dequeue)
        self.head = None
        # хвіст : елемент, куди буде додано новий елемент (enqueue)
        self.tail = None
        self.size = 0

    # додавання в кінець
    def enqueue(self, data):
        new_node = Node(data)
        # якщо черга порожня, head і tail вказують на новий вузол
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # поточний хвіст вказує на новий вузол
            self.tail.next = new_node
            # новий вузол стає новим хвостом
            self.tail = new_node

        self.size += 1
        print(f"ENQUEUE: Додано {data}")

    # видалення з початку
    def dequeue(self):
        # перевірка, чи черга не порожня
        if self.is_empty():
            print("DEQUEUE: Черга порожня.")
            return None

        # зберігаємо дані поточної голови для повернення
        dequeued_data = self.head.data

        # переміщуємо голову на наступний елемент
        self.head = self.head.next

        # якщо голова стала None, черга спорожніла, оновлюємо хвіст
        if self.head is None:
            self.tail = None

        self.size -= 1
        print(f"DEQUEUE: Видалено {dequeued_data}")
        return dequeued_data

    # перегляд першого
    def peek(self):
        if self.is_empty():
            return "Черга порожня"

        return self.head.data

    # порожність
    def is_empty(self):
        return self.head is None

    # розмір
    def get_size(self):
        return self.size


# Робота
my_queue = Queue()


my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)


print(f"PEEK: Перший елемент: {my_queue.peek()}")


my_queue.dequeue()
my_queue.dequeue()

print(f"PEEK: Наступний елемент: {my_queue.peek()}")
print(f"Розмір черги: {my_queue.get_size()}") 