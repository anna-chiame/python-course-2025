# Підрахунок рядків і символів через seek(0)
print("Файл відкривається один раз через повернення курсору")

def count_lines(f):
    text = f.read()                                # читаємо весь файл як один рядок
    f.seek(0)                                      # повертаємо курсор на початок
    return text.count("\n") + 1 if text else 0  # кількість рядків, через кількість \n

def count_chars(f):
    text = f.read()
    f.seek(0)
    return len(text)           # кількість символів

def test(name):
    f = open(name, encoding='utf-8')  # відкриваємо файл один раз
    lines = count_lines(f)            # підраховуємо рядки
    chars = count_chars(f)            # підраховуємо символи
    print(f"File '{name}' has {lines} lines and {chars} characters.")
    f.close()                         # закриваємо файл