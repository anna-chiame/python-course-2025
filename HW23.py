from typing import List, Tuple

# We assume that all lists passed to functions are the same length N

Match
big
O
complexities
with the code snippets below

# answers
# 1 - log n
# 2 - n^2
# 3 - n
# 4 - n^2
# 5 - 1
# 6 - n

# 1 O(n)*O(n)=O(n^2)
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    # проходимо по кожному елементу першого списку - O(n)
    for el_first_list in first_list:
        # пошук у другому списку — лінійна операція - O(n)
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

# 2 O(1)
def question2(n: int) -> int:
    # цикл виконується рівно 10 разів: константна кількість  O(1)
    for _ in range(10):
      # піднесення до степеня : одна операція  O(1)
        n **= 3
    return n

# 3 0(n^2+n+1) - 0(n^2)
def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    # копіюємо перший список O(n)
    temp: List[int] = first_list[:]
    # цикл по другому списку  O(n)
    for el_second_list in second_list:
        flag = False
        # перевірка кожного елемента першого списку O(n)
        for check in temp:
            #порівняння  O(1)
            if el_second_list == check:
                flag = True
                break
        if not flag:
            # додавання, якщо не знайдено O(1)
            temp.append(second_list)
    return temp

# 4 Бере завжди гірший тобто O(n)
def question4(input_list: List[int]) -> int:
    res: int = 0
    # цикл проходить по кожному елементу  O(n)
    for el in input_list:
        # порівняння  O(1)
        if el > res:
            # присвоєння  O(1)
            res = el
    return res

# 5 0(n^2)
def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    # перший цикл  O(n)
    for i in range(n):
        # вкладений цикл O(n)
        for j in range(n):
            #додавання пари O(1)
            res.append((i, j))
    return res

#6 log₂(n)
def question6(n: int) -> int:
    # цикл триває, поки n не стане ≤ 1
    while n > 1:
        #а  кожен крок ділить n навпіл повтор по кылькості циклу-логарифм log₂(n)
        n /= 2
    return n
