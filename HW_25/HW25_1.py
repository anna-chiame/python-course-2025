#1
class Node:
    """Клас для представлення вузла зв'язаного списку."""
    def __init__(self, data):
        self.data = data
        self.next = None

class UnsortedList:
    """Реалізація однозв'язного списку."""
    def __init__(self):
        self.head = None
        # початок, поки немає ніяких елементів
        self._length = 0
    # чи порожній
    def is_empty(self):
        return self.head is None
    # показуэ розмір списку
    def size(self):
        return self._length

    # додає в кінець списку
    def append(self, item):
        """Додає вузол в кінець списку"""

        new_node = Node(item)
        # збільшуємо лічильник списку
        self._length +=1
    # Якщо список порожній то новий вузол стає головою списку
        if self.is_empty():
            self.head = new_node
            return
    # Якщо не порожній список, то шукаємо хвіст де показчик next == None
        # починаємо з голови
        current = self.head
        while current.next is not None :
            current = current.next
        # встановлюємо покажчик next останнього вузла на наш new_node
        current.next = new_node

    def index(self, item):
        """Видає позицію (індекс) першого входження елемента"""
        current = self.head
        index_counter = 0

        # Обхід списку від початку
        while current is not None:
            if current.data == item:
                # eлемент знайдено, повертаємо його індекс.
                return index_counter
            # переходимо до наступного вузла.
            current = current.next
            # збільшуємо лічильник індексу.
            index_counter += 1

        # якщо цикл завершився, і елемент не знайдено
        raise ValueError(f"Елемент '{item}' не знайдено у списку")

    def pop(self, ind=None):
        """
        Видаляє та повертає елемент за індексом 'ind'.
        Якщо pos=None, видаляє останній елемент. O(n)
        """
        if self.is_empty():
            raise IndexError("Видалення з порожнього списку")

        # Визначаємо ind. Якщо ind=None, видаляємо останній елемент.
        item_ind = ind if ind is not None else self._length - 1
        # перевірка меж
        if item_ind < 0 or item_ind >= self._length:
            raise IndexError("Індекс pop виходить за межі")
        # зменшуємо розмір, оскільки елемент буде видалено.
        self._length -= 1
        # видалення першого елемента (ind=0), потрыбна нова голова
        if item_ind == 0:
            removed_item = self.head.data
            # нова голова —> наступний вузол.
            self.head = self.head.next
            return removed_item

        # видалення всередині або в кінці
        current = self.head
        previous = None
        current_ind = 0

        # рухаємося до вузла, який треба видалити
        while current is not None and current_ind < item_ind:
            # previous завжди вказує на вузол перед current.
            previous = current
            current = current.next
            current_ind += 1
        # зберігаємо дані видаленого вузла.
        removed_item = current.data

        # перестрибуємо через вузол: попередній вузол тепер вказує на наступний за видаленим.
        previous.next = current.next

        return removed_item

    def insert(self, ind, item):
        """Вставляє елемент за вказаною позицією ind"""
        new_node = Node(item)
        self._length += 1

        # вставка на початку
        if pos == 0:
            # новий вузол вказує на стару голову.
            new_node.next = self.head
            # новий вузол стає новою Головою.
            self.head = new_node
            return

        # вставка всередині або в кінці
        current = self.head
        previous = None
        current_ind = 0

        # прохід до позиції, перед якою потрібно вставити (тобто до ind-1)
        while current is not None and current_ind < ind:
            previous = current
            current = current.next
            current_ind += 1

        # previous тепер є вузлом, після якого ми вставляємо.
        # новий вузол вказує на вузол, який був на ind.
        new_node.next = current
        # попередній вузол вказує на новий вузол.
        previous.next = new_node

    def slice(self, start, stop):
        """
        Повертає копію списку від 'start' до 'stop' (не включно)
        """
        new_list = UnsortedList()
        current = self.head
        current_ind = 0

        # обхід до початкової позиції (start)
        while current is not None and current_ind < start:
            current = current.next
            current_ind += 1

        # обхід та копіювання до кінцевої позиції (stop)
        # current тепер знаходиться на позиції 'start'.
        while current is not None and current_ind < stop:
            # копіюємо дані поточного вузла в кінець нового списку.
            new_list.append(current.data)
            current = current.next
            current_ind += 1

        return new_list  
