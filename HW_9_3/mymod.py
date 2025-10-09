#файл відкривається двічі
print("Файл відкривається двічі")
#підрахунок ліній
def count_lines(name) :
    f = open(name, encoding='utf-8')          # відкриваємо файл для читання,
                                              # обов'язково перекодування бо видасть помилку
    lines = f.readlines()        # зчитуємо всі рядки як список
    f.close()                    # закриваємо файл
    return len(lines)            # рахуємо кількість рядків

#підрахунок символів
def count_chars(name) :
    f = open(name, encoding='utf-8')         # відкриваємо файл для читання
                                             # обов'язково перекоування бо выдасть помилку
    chars = f.read()            # читаємо весь вміст файлу як один рядок
    f.close()                   # закриваємо файл
    return len(chars)           # рахуємо кількість символів

# викликає функції підрахунку
def test(name) :
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"File '{name}' has {lines} lines and {chars} characters.") # вивід результату
