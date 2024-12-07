import tkinter as tk
from tkinter import simpledialog
import json
import random
import math

# Файл для сохранения данных
DATA_FILE = 'math_game_data.json'

# Загрузка и сохранение данных
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data():
    default_data = {
        "classes": {
            "5 класс": ["Сложение натуральных чисел","Вычитание натуральных чисел","Сложение дробей","Вычитание дробей","Рациональные числа"],
            "6 класс": ["Сложение натуральных чисел","Вычитание натуральных чисел","Умножение натуральных чисел","Деление натуральных чисел","Сложение дробей","Вычитание дробей","Умножение дробей","Деление дробей"],
            "7 класс": ["Уравнения","Простые уравнения","Проценты","Углы","Уравнения с делением","Площадь прямоугольника"],
            "8 класс": ["треугольник","квадрат","прямоугольник","Простые уравнения с двумя переменными","Проценты от скидки","Углы, смежные","Квадратное уравнение","Площадь треугольника","Находить медиану","Система уравнений"],
            "9 класс": ["Тригонометрия","Квадратные уравнения","Уравнения третьей степени","Геометрия в пространстве","Статистика и вероятности","Тригонометрия","Производные","Интегралы"],
            "10 класс": ["Квадратные уравнения","Тригонометрические функции","Аналитическая геометрия","Производные","Интегралы","Комбинаторика","Вероятность"],
            "11 класс": ["Квадратные уравнения","Дифференциальные уравнения","Сложные интегралы","Аналитическая геометрия в пространстве","Векторная алгебра","Статистика","Логарифмы","Производные","Интегралы"]
        },
        "custom_examples": {}
    }

    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Проверим, что "custom_examples" существует
            if "custom_examples" not in data:
                data["custom_examples"] = {}
            # Проверим, есть ли предустановленные классы, и добавим их, если они отсутствуют
            for class_name, topics in default_data["classes"].items():
                if class_name not in data["classes"]:
                    data["classes"][class_name] = topics
            return data
    except FileNotFoundError:
        return default_data

# Загрузка данных при запуске программы
data = load_data()

# Генерация примеров на основе темы
def generate_example(selected_class, topic):
# для 5 классов
    if "Сложение натуральных чисел" in topic:
        num1, num2 = random.randint(1, 50), random.randint(1, 50)
        example = f"{num1} + {num2}"
        answer = num1 + num2
    elif "Вычитание натуральных чисел" in topic:
        num1, num2 = random.randint(20, 100), random.randint(1, 20)
        example = f"{num1} - {num2}"
        answer = num1 - num2
    elif "Сложение дробей" in topic:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        den1, den2 = random.randint(1, 10), random.randint(1, 10)
        example = f"{num1}/{den1} + {num2}/{den2}"
        answer = round(num1 / den1 + num2 / den2, 2)
    elif "Вычитание дробей" in topic:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        den1, den2 = random.randint(1, 10), random.randint(1, 10)
        example = f"{num1}/{den1} - {num2}/{den2}"
        answer = round(num1 / den1 - num2 / den2, 2)
    elif "Рациональные числа" in topic:
        num1, num2 = random.randint(-50, 50), random.randint(-50, 50)
        example = f"{num1} + {num2}"
        answer = num1 + num2
# для 6 классов
    elif "Сложение натуральных чисел" in topic:
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        example = f"{num1} + {num2}"
        answer = num1 + num2

    elif "Вычитание натуральных чисел" in topic:
        num1, num2 = random.randint(20, 100), random.randint(1, 20)
        example = f"{num1} - {num2}"
        answer = num1 - num2

    elif "Умножение натуральных чисел" in topic:
        num1, num2 = random.randint(1, 12), random.randint(1, 12)
        example = f"{num1} * {num2}"
        answer = num1 * num2

    elif "Деление натуральных чисел" in topic:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 10)  # делитель не должен быть 0
        example = f"{num1} / {num2}"
        answer = round(num1 / num2, 2)  # Ответ округляется до двух знаков после запятой

    elif "Сложение дробей" in topic:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        den1, den2 = random.randint(1, 10), random.randint(1, 10)
        example = f"{num1}/{den1} + {num2}/{den2}"
        answer = round(num1 / den1 + num2 / den2, 2)  # Ответ округляется до двух знаков после запятой

    elif "Вычитание дробей" in topic:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        den1, den2 = random.randint(1, 10), random.randint(1, 10)
        example = f"{num1}/{den1} - {num2}/{den2}"
        answer = round(num1 / den1 - num2 / den2, 2)  # Ответ округляется до двух знаков после запятой

    elif "Умножение дробей" in topic:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        den1, den2 = random.randint(1, 10), random.randint(1, 10)
        example = f"{num1}/{den1} * {num2}/{den2}"
        answer = round((num1 * num2) / (den1 * den2), 2)  # Ответ округляется до двух знаков после запятой

    elif "Деление дробей" in topic:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        den1, den2 = random.randint(1, 10), random.randint(1, 10)
        example = f"{num1}/{den1} / {num2}/{den2}"
        answer = round((num1 / den1) / (num2 / den2), 2)  # Ответ округляется до двух знаков после запятой
# для 7 классов
    elif "Уравнения" in topic:
        a = random.randint(1, 10)  # коэффициент при x
        b = random.randint(1, 10)  # свободный член
        c = random.randint(1, 20)  # результат
        example = f"{a}x + {b} = {c}"
        answer = (c - b) / a

    elif "Простые уравнения" in topic:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        example = f"{a}x + {b} = 0"
        answer = f"x = {-b / a}"

    elif "Проценты" in topic:
        total = random.randint(100, 1000)
        percent = random.randint(1, 100)
        example = f"{percent}% от {total}"
        answer = round(total * percent / 100, 2)

    elif "Углы" in topic:
        angle1 = random.randint(1, 180)
        example = f"Какой угол дополняет угол {angle1} градусов до 180 градусов?"
        answer = round(180 - angle1, 2)

    elif "Уравнения с делением" in topic:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        example = f"{a}x = {b}"
        answer = f"x = {b / a}"

    elif "Площадь прямоугольника" in topic:
        length = random.randint(1, 20)
        width = random.randint(1, 20)
        example = f"Какова площадь прямоугольника со сторонами {length} и {width}?"
        answer = length * width
# для 8 классов
    elif "треугольник" in topic:
        a = random.randint(5, 10)
        b = random.randint(5, 10)
        c = random.randint(5, 10)
        example = f"Найдите perimeter треугольника со сторонами {a}, {b}, {c}."
        answer = a + b + c
    elif "квадрат" in topic:
        side = random.randint(1, 10)
        example = f"Найдите площадь квадрата со стороной {side}."
        answer =  2
    elif  "прямоугольник"  in topic:
        length = random.randint(1, 10)
        width = random.randint(1, 10)
        example = f"Найдите площадь прямоугольника со сторонами {length} и {width}."
        answer = length * width
    elif "Простые уравнения с двумя переменными" in topic:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 20)
        example = f"{a}x + {b}y = {c}"
        answer = f"x = ({c - b}y) / {a}"

    elif "Проценты от скидки" in topic:
        original_price = random.randint(100, 1000)
        discount = random.randint(1, 100)
        example = f"Скидка {discount}% на товар, стоимостью {original_price} рублей."
        answer = round(original_price * (1 - discount / 100), 2)

    elif "Углы, смежные" in topic:
        angle1 = random.randint(1, 179)
        example = f"Какой угол смежный с углом {angle1} градусов?"
        answer = 180 - angle1

    elif "Квадратное уравнение" in topic:
        a = random.randint(1, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        example = f"{a}x^2 + {b}x + {c} = 0"
        D = b ** 2 - 4 * a * c
        answer = f"x = {(-b + D ** 0.5) / (2 * a)}, x = {(-b - D ** 0.5) / (2 * a)}" if D >= 0 else "Нет реальных корней"

    elif "Площадь треугольника" in topic:
        base = random.randint(1, 20)
        height = random.randint(1, 20)
        example = f"Какова площадь треугольника с основанием {base} и высотой {height}?"
        answer = 0.5 * base * height

    elif "Находить медиану" in topic:
        numbers = sorted([random.randint(1, 100) for _ in range(3)])
        example = f"Найдите медиану для чисел: {numbers}"
        answer = numbers[1]

    elif "Система уравнений" in topic:
        a1 = random.randint(1, 5)
        b1 = random.randint(1, 5)
        c1 = random.randint(1, 10)
        a2 = random.randint(1, 5)
        b2 = random.randint(1, 5)
        c2 = random.randint(1, 10)
        example = f"{a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}"
        # Упрощенный ответ
        answer = "Найдите x и y методом подстановки или исключения."
#для 9 классов
    elif "Тригонометрия" in topic:
        angle = random.choice([30, 45, 60, 90])
        example = f"sin({angle})"
        answer = round(math.sin(math.radians(angle)), 2)

    elif "Квадратные уравнения" in topic:
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        c = random.randint(1, 5)
        example = f"{a}x^2 + {b}x + {c} = 0"
        discriminant =  2 - 4 * a * c
        if discriminant > 0:
            root1 = round((-b + math.sqrt(discriminant)) / (2 * a), 2)
            root2 = round((-b - math.sqrt(discriminant)) / (2 * a), 2)
            answer = f"Есть два действительных корня: x1 = {root1}, x2 = {root2}"
        elif discriminant == 0:
            root = round(-b / (2 * a), 2)
            answer = f"Есть один кратный корень: x = {root}"
        else:
            answer = "Нет действительных корней"

    elif "Уравнения третьей степени" in topic:
        a = random.randint(1, 3)
        b = random.randint(-3, 3)
        c = random.randint(-3, 3)
        d = random.randint(-3, 3)
        example = f"{a}x^3 + {b}x^2 + {c}x + {d} = 0"
        answer = "Найдите корни уравнения (можно использовать графический метод или численный метод)."

    elif "Геометрия в пространстве" in topic:
        shape = random.choice(["цилиндр", "конический сечений", "куб", "параллелепипед"])
        if "цилиндр" in topic:
            radius = random.randint(1, 5)
            height = random.randint(5, 10)
            example = f"Найдите объем цилиндра радиусом {radius} и высотой {height}."
            answer = round(math.pi * 2)
        elif "куб" in topic:
            side = random.randint(1, 5)
            example = f"Найдите объем куба со стороной {side}."
            answer =  3
        else:  # параллелепипед
            length = random.randint(1, 5)
            width = random.randint(1, 5)
            height = random.randint(5, 10)
            example = f"Найдите объем параллелепипеда с длиной {length}, шириной {width} и высотой {height}."
            answer = length * width * height

    elif "Статистика и вероятности" in topic:
        data = [random.randint(1, 100) for _ in range(10)]
        example = f"Даны данные: {data}. Найдите среднее значение."
        answer = round(sum(data) / len(data), 2)

    elif "Тригонометрия" in topic:
        angle = random.choice([30, 45, 60, 90])
        example = f"cos({angle})"
        answer = round(math.cos(math.radians(angle)), 2)

    elif "Производные" in topic:
        example = "Найдите производную от 3x^2 + 2x + 1"
        answer = "6x + 2"

    elif "Интегралы" in topic:
        example = "Вычислите неопределенный интеграл от 3x^2 + 2x"
        answer = "x^3 + x^2 + C"
#для 10 классов
    elif "Квадратные уравнения" in topic:
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        c = random.randint(1, 5)
        example = f"{a}x^2 + {b}x + {c} = 0"
        discriminant = 2 - 4 * a * c
        if discriminant > 0:
            root1 = round((-b + math.sqrt(discriminant)) / (2 * a), 2)
            root2 = round((-b - math.sqrt(discriminant)) / (2 * a), 2)
            answer = f"Есть два действительных корня: x1 = {root1}, x2 = {root2}"
        elif discriminant == 0:
            root = round(-b / (2 * a), 2)
            answer = f"Есть один кратный корень: x = {root}"
        else:
            answer = "Нет действительных корней"

    elif "Тригонометрические функции" in topic:
        angle = random.choice([30, 45, 60, 90])
        example = f"Определите значение sin({angle}) и cos({angle})"
        sin_value = round(math.sin(math.radians(angle)), 2)
        cos_value = round(math.cos(math.radians(angle)), 2)
        answer = f"sin({angle}) = {sin_value}, cos({angle}) = {cos_value}"

    elif "Аналитическая геометрия" in topic:
        x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
        x2, y2 = random.randint(-5, 5), random.randint(-5, 5)
        example = f"Найдите расстояние между точками A({x1}, {y1}) и B({x2}, {y2})"
        distance = round(math.sqrt((x2 - x1) **2 + (y2 - y1)**2  ), 2)
        answer = f"Расстояние между точками A и B = {distance}"

    elif "Производные" in topic:
        example = "Найдите производную от 2x^3 + 3x^2 - 5x + 1"
        answer = "6x^2 + 6x - 5"

    elif "Интегралы" in topic:
        example = "Вычислите неопределенный интеграл от 4x^3"
        answer = "x^4 + C"

    elif "Комбинаторика" in topic:
        n = random.randint(5, 10)
        r = random.randint(1, n)
        example = f"Сколько способов выбрать {r} предметов из {n}?"
        answer = math.comb(n, r)

    elif "Вероятность" in topic:
        # Пример с вероятностью
        favorable_outcomes = random.randint(1, 5)
        total_outcomes = random.randint(6, 10)
        example = f"Какова вероятность выпадения благоприятного исхода из {total_outcomes} возможных, при {favorable_outcomes} благоприятных?"
        probability = round(favorable_outcomes / total_outcomes, 2)
        answer = f"P = {probability}"
# для 11 классов
    elif "Квадратные уравнения" in topic:
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        c = random.randint(1, 5)
        example = f"{a}x^2 + {b}x + {c} = 0"
        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:
            root1 = round((-b + math.sqrt(discriminant)) / (2 * a), 2)
            root2 = round((-b - math.sqrt(discriminant)) / (2 * a), 2)
            answer = f"Есть два действительных корня: x1 = {root1}, x2 = {root2}"
        elif discriminant == 0:
            root = round(-b / (2 * a), 2)
            answer = f"Есть один кратный корень: x = {root}"
        else:
            answer = "Нет действительных корней"

    elif "Дифференциальные уравнения" in topic:
        example = "Решите дифференциальное уравнение dy/dx = y"
        answer = "y = C*e^x"

    elif "Сложные интегралы" in topic:
        example = "Вычислите интеграл от sin(x)dx"
        answer = "-cos(x) + C"

    elif "Аналитическая геометрия в пространстве" in topic:
        x1, y1, z1 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)
        x2, y2, z2 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)
        example = f"Найдите расстояние между точками A({x1}, {y1}, {z1}) и B({x2}, {y2}, {z2})"
        distance = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2), 2)
        answer = f"Расстояние между точками A и B = {distance}"

    elif "Векторная алгебра" in topic:
        x1, y1 = random.randint(1, 5), random.randint(1, 5)
        x2, y2 = random.randint(1, 5), random.randint(1, 5)
        example = f"Найдите сумму векторов A({x1}, {y1}) и B({x2}, {y2})"
        sum_vector = (x1 + x2, y1 + y2)
        answer = f"Сумма векторов A и B = A({sum_vector[0]}, {sum_vector[1]})"

    elif "Статистика" in topic:
        data = [random.randint(1, 100) for _ in range(10)]
        example = f"Даны данные: {data}. Найдите среднее значение."
        answer = round(sum(data) / len(data), 2)

    elif "Логарифмы" in topic:
        base, x = random.randint(2, 10), random.randint(1, 100)
        example = f"log_{base}({x})"
        answer = round(math.log(x, base), 2)

    elif "Производные" in topic:
        example = "Найдите производную от x^3"
        answer = "3x^2"

    elif "Интегралы" in topic:
        example = "Вычислите неопределенный интеграл от x^2"
        answer = "1/3 * x^3 + C"

    return example, answer
# Функция очистки окна
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Функция управления классами
def manage_classes(action):
    if action == "Добавить":
        new_class = simpledialog.askstring("Добавить класс", "Введите название нового класса:", parent=root)
        if new_class and new_class not in data["classes"]:
            data["classes"][new_class] = []
            save_data(data)
            start_game_screen()

    elif action == "Удалить":
        modal_window = tk.Toplevel(root)
        modal_window.title("Удалить класс")
        modal_window.geometry("400x200")

        class_to_delete = tk.StringVar(modal_window)
        class_to_delete.set(list(data["classes"].keys())[0])  # Устанавливаем первый класс по умолчанию
        option_menu = tk.OptionMenu(modal_window, class_to_delete, *data["classes"].keys())
        option_menu.pack(pady=10)

        def delete_selected_class():
            del data["classes"][class_to_delete.get()]
            save_data(data)
            start_game_screen()
            modal_window.destroy()

        delete_button = tk.Button(modal_window, text="Удалить", command=delete_selected_class)
        delete_button.pack(pady=10)

    elif action == "Изменить":
        modal_window = tk.Toplevel(root)
        modal_window.title("Изменить класс")
        modal_window.geometry("400x200")

        class_to_edit = tk.StringVar(modal_window)
        class_to_edit.set(list(data["classes"].keys())[0])  # Устанавливаем первый класс по умолчанию
        option_menu = tk.OptionMenu(modal_window, class_to_edit, *data["classes"].keys())
        option_menu.pack(pady=10)

        def save_class_change():
            selected_class = class_to_edit.get()  # Получаем выбранный класс
            if selected_class in data["classes"]:  # Проверяем, существует ли выбранный класс
                new_name = simpledialog.askstring("Изменить класс", "Введите новое название для класса:",
                                                  parent=modal_window)
                if new_name and new_name not in data["classes"]:  # Проверяем, что новое название не дублируется
                    # Меняем название класса
                    data["classes"][new_name] = data["classes"].pop(selected_class)
                    save_data(data)  # Сохраняем изменения
                    start_game_screen()  # Обновляем экран игры
                    modal_window.destroy()  # Закрываем модальное окно
                elif new_name in data["classes"]:
                    tk.messagebox.showerror("Ошибка", "Класс с таким названием уже существует.")
            else:
                tk.messagebox.showerror("Ошибка", "Выбранный класс не существует.")

        save_button = tk.Button(modal_window, text="Сохранить изменения", command=save_class_change)
        save_button.pack(pady=10)

# Функция управления темами
def manage_topics(action, selected_class):
    if action == "Добавить":
        new_topic = simpledialog.askstring("Добавить тему", "Введите название новой темы:", parent=root)
        if new_topic and new_topic not in data["classes"][selected_class]:
            data["classes"][selected_class].append(new_topic)
            save_data(data)
            select_topic_screen(selected_class)

    elif action == "Удалить":
        modal_window = tk.Toplevel(root)
        modal_window.title("Удалить тему")
        modal_window.geometry("400x200")

        topic_to_delete = tk.StringVar(modal_window)
        topic_to_delete.set(data["classes"][selected_class][0])  # Устанавливаем первую тему по умолчанию
        option_menu = tk.OptionMenu(modal_window, topic_to_delete, *data["classes"][selected_class])
        option_menu.pack(pady=10)

        def delete_topic():
            data["classes"][selected_class].remove(topic_to_delete.get())
            save_data(data)
            select_topic_screen(selected_class)
            modal_window.destroy()

        delete_button = tk.Button(modal_window, text="Удалить", command=delete_topic)
        delete_button.pack(pady=10)

    elif action == "Изменить":
        modal_window = tk.Toplevel(root)
        modal_window.title("Изменить тему")
        modal_window.geometry("400x200")

        topic_to_edit = tk.StringVar(modal_window)
        topic_to_edit.set(data["classes"][selected_class][0])  # Устанавливаем первую тему по умолчанию
        option_menu = tk.OptionMenu(modal_window, topic_to_edit, *data["classes"][selected_class])
        option_menu.pack(pady=10)

        def save_topic_change():
            new_name = simpledialog.askstring("Изменить тему", "Введите новое название для темы:", parent=modal_window)
            if new_name:
                idx = data["classes"][selected_class].index(topic_to_edit.get())
                data["classes"][selected_class][idx] = new_name
                save_data(data)
                select_topic_screen(selected_class)
                modal_window.destroy()

        save_button = tk.Button(modal_window, text="Сохранить изменения", command=save_topic_change)
        save_button.pack(pady=10)

# Функция управления примерами
def manage_examples(action, selected_class, topic, examples_frame=None):
    def open_modal():
        if action == "Добавить":
            # Без создания отдельного модального окна для ввода
            new_example = simpledialog.askstring("Добавить пример", "Введите новый пример:", parent=root)
            if new_example:
                answer = simpledialog.askinteger("Добавить пример", "Введите правильный ответ:", parent=root)
                if selected_class not in data["custom_examples"]:
                    data["custom_examples"][selected_class] = {}
                if topic not in data["custom_examples"][selected_class]:
                    data["custom_examples"][selected_class][topic] = []
                data["custom_examples"][selected_class][topic].append({"example": new_example, "answer": answer})
                save_data(data)
                # Обновляем список примеров
                update_examples_list(selected_class, topic, examples_frame)

        elif action == "Удалить":
            modal_window = tk.Toplevel(root)
            modal_window.title("Удалить пример")
            modal_window.geometry("400x200")

            example_to_delete = tk.StringVar(modal_window)
            examples = [ex["example"] for ex in data["custom_examples"].get(selected_class, {}).get(topic, [])]
            if examples:
                example_to_delete.set(examples[0])
                option_menu = tk.OptionMenu(modal_window, example_to_delete, *examples)
                option_menu.pack(pady=10)

                def delete_example():
                    data["custom_examples"][selected_class][topic] = [
                        ex for ex in data["custom_examples"][selected_class][topic]
                        if ex["example"] != example_to_delete.get()
                    ]
                    save_data(data)
                    modal_window.destroy()
                    # Обновляем список примеров
                    update_examples_list(selected_class, topic, examples_frame)

                delete_button = tk.Button(modal_window, text="Удалить пример", command=delete_example)
                delete_button.pack(pady=10)

        elif action == "Изменить":
            modal_window = tk.Toplevel(root)
            modal_window.title("Изменить пример")
            modal_window.geometry("400x200")

            example_to_edit = tk.StringVar(modal_window)
            examples = [ex["example"] for ex in data["custom_examples"].get(selected_class, {}).get(topic, [])]
            if examples:
                example_to_edit.set(examples[0])
                option_menu = tk.OptionMenu(modal_window, example_to_edit, *examples)
                option_menu.pack(pady=10)

                def update_example():
                    for ex in data["custom_examples"][selected_class][topic]:
                        if ex["example"] == example_to_edit.get():
                            new_example = simpledialog.askstring("Изменить пример", "Введите новый текст примера:", parent=modal_window)
                            new_answer = simpledialog.askinteger("Изменить пример", "Введите новый правильный ответ:", parent=modal_window)
                            ex["example"] = new_example
                            ex["answer"] = new_answer
                            save_data(data)
                            modal_window.destroy()
                            # Обновляем список примеров
                            update_examples_list(selected_class, topic, examples_frame)
                            break

                save_button = tk.Button(modal_window, text="Сохранить изменения", command=update_example)
                save_button.pack(pady=10)

    open_modal()

# Функция для обновления списка примеров
def update_examples_list(selected_class, topic, examples_frame):
    for widget in examples_frame.winfo_children():
        widget.destroy()

    examples = data.get("custom_examples", {}).get(selected_class, {}).get(topic, [])

    if examples:
        for i, example in enumerate(examples):
            example_label = tk.Label(examples_frame, text=f"{example['example']} = {example['answer']}",
                                     font=("Arial", 14))
            example_label.grid(row=i, column=0, padx=10, pady=5)
    else:
        no_examples_label = tk.Label(examples_frame, text="Нет добавленных примеров", font=("Arial", 14))
        no_examples_label.pack(pady=10)

# Функция для отображения примеров
def show_custom_examples(selected_class, topic):
    examples_window = tk.Toplevel(root)
    examples_window.title(f"Мои примеры для {topic}")
    examples_window.geometry("600x400")

    examples_frame = tk.Frame(examples_window)
    examples_frame.pack(pady=10)

    # Обновляем примеры при открытии окна
    update_examples_list(selected_class, topic, examples_frame)

    add_button = tk.Button(examples_window, text="Добавить пример", command=lambda: manage_examples("Добавить", selected_class, topic, examples_frame))
    add_button.pack(side=tk.LEFT, padx=10, pady=10)

    delete_button = tk.Button(examples_window, text="Удалить пример", command=lambda: manage_examples("Удалить", selected_class, topic, examples_frame))
    delete_button.pack(side=tk.LEFT, padx=10, pady=10)

    edit_button = tk.Button(examples_window, text="Изменить пример", command=lambda: manage_examples("Изменить", selected_class, topic, examples_frame))
    edit_button.pack(side=tk.LEFT, padx=10, pady=10)

# Функция выбора темы для выбранного класса
def select_topic_screen(selected_class):
    clear_window()
    label = tk.Label(root, text=f"Выберите тему для {selected_class}", font=("Arial", 24), wraplength=700)
    label.pack(pady=20)

    topics_frame = tk.Frame(root)
    topics_frame.pack()

    # Отображаем все темы, включая стандартные и добавленные пользователем
    topics = data["classes"].get(selected_class, [])

    if not topics:
        label = tk.Label(topics_frame, text="Нет доступных тем", font=("Arial", 16))
        label.pack(pady=10)
    else:
        for i, topic in enumerate(topics):
            topic_button = tk.Button(topics_frame, text=topic, font=("Arial", 16),
                                     command=lambda t=topic: select_mode_screen(selected_class, t))
            topic_button.grid(row=i // 2, column=i % 2, padx=20, pady=10)

    manage_frame = tk.Frame(root)
    manage_frame.pack(pady=20)

    add_button = tk.Button(manage_frame, text="Добавить тему", font=("Arial", 16),
                           command=lambda: manage_topics("Добавить", selected_class))
    add_button.grid(row=0, column=0, padx=10)

    delete_button = tk.Button(manage_frame, text="Удалить тему", font=("Arial", 16),
                              command=lambda: manage_topics("Удалить", selected_class))
    delete_button.grid(row=0, column=1, padx=10)

    edit_button = tk.Button(manage_frame, text="Изменить тему", font=("Arial", 16),
                            command=lambda: manage_topics("Изменить", selected_class))
    edit_button.grid(row=0, column=2, padx=10)

    back_button = tk.Button(root, text="Назад", font=("Arial", 16), command=start_game_screen)
    back_button.pack(pady=20)

# Функция выбора режима игры для темы
def select_mode_screen(selected_class, topic):
    clear_window()
    label = tk.Label(root, text=f"Вы выбрали тему '{topic}' для {selected_class}", font=("Arial", 24), wraplength=700)
    label.pack(pady=20)

    # Добавляем галочку для выбора использования примеров учителя
    global use_custom_examples
    use_custom_examples = tk.BooleanVar(value=True)
    checkbox = tk.Checkbutton(root, text="Использовать примеры учителя", variable=use_custom_examples)
    checkbox.pack(pady=10)

    button_with_answers = tk.Button(root, text="С ответами", font=("Arial", 16),
                                    command=lambda: start_game_with_answers(selected_class, topic))
    button_without_answers = tk.Button(root, text="Без ответов", font=("Arial", 16),
                                       command=lambda: start_game_without_answers(selected_class, topic))
    button_with_answers.pack(pady=10)
    button_without_answers.pack(pady=10)

    show_examples_button = tk.Button(root, text="Показать мои примеры", font=("Arial", 16),
                                     command=lambda: show_custom_examples(selected_class, topic))
    show_examples_button.pack(pady=10)

    back_button = tk.Button(root, text="Назад", font=("Arial", 16), command=lambda: reset_and_go_back(selected_class))
    back_button.pack(pady=20)

#функцию для сброса галочки и возврата на предыдущий экран
def reset_and_go_back(selected_class):
    use_custom_examples.set(False)  # Сбрасываем состояние галочки
    select_topic_screen(selected_class)

# Функция игры с ответами
def start_game_with_answers(selected_class, topic):
    clear_window()

    # Индекс текущего примера
    global current_example_index
    current_example_index = 0

    # Функция для показа следующего примера
    def show_next_example():
        global current_example_index
        custom_examples = data["custom_examples"].get(selected_class, {}).get(topic, [])

        # Определяем, нужно ли показывать пример учителя или генерировать новый
        if use_custom_examples.get() and custom_examples:
            if current_example_index < len(custom_examples):
                example_info = custom_examples[current_example_index]
                current_example_index += 1
                example = example_info['example']
                correct_answer = example_info['answer']
            else:
                example, correct_answer = generate_example(selected_class, topic)
        else:
            example, correct_answer = generate_example(selected_class, topic)

        return example, correct_answer

    # Функция для обновления экрана с новым примером
    def update_example():
        for widget in root.winfo_children():
            widget.destroy()

        example, correct_answer = show_next_example()

        # Выводим пример на экран
        label = tk.Label(root, text=f"Пример: {example}", font=("Arial", 24))
        label.pack(pady=20)

        # Генерация ответов
        wrong_answers = [correct_answer + random.randint(1, 5), correct_answer - random.randint(1, 5)]
        choices = [correct_answer] + wrong_answers
        random.shuffle(choices)

        # Отображаем варианты ответов
        choices_frame = tk.Frame(root)
        choices_frame.pack(pady=20)
        answer_buttons = []
        for i, choice in enumerate(choices):
            choice_button = tk.Button(choices_frame, text=str(choice), font=("Arial", 16),
                                      command=lambda idx=i: select_answer(idx, answer_buttons, correct_answer))
            choice_button.grid(row=0, column=i, padx=10)
            answer_buttons.append(choice_button)

        # Кнопка для показа правильного ответа
        show_answer_button = tk.Button(root, text="Показать ответ", font=("Arial", 16),
                                       command=lambda: show_answer(correct_answer, answer_buttons))
        show_answer_button.pack(pady=10)

        # Кнопка для перехода к следующему примеру
        next_example_button = tk.Button(root, text="Следующий пример", font=("Arial", 16),
                                        command=update_example)
        next_example_button.pack(pady=10)

        # Кнопка для возврата на предыдущий экран
        back_button = tk.Button(root, text="Назад", font=("Arial", 16),
                                command=lambda: select_mode_screen(selected_class, topic))
        back_button.pack(pady=20)

    # Изначально показываем первый пример
    update_example()

# Показать правильный ответ для чисел с плавающей точкой
def show_answer(correct_answer, buttons):
    for btn in buttons:
        try:
            if float(btn['text']) == correct_answer:
                btn.config(bg="green")
        except ValueError:
            continue  # Если это не число, пропускаем

# Выбрать ответ с учетом чисел с плавающей точкой
def select_answer(idx, buttons, correct_answer):
    for btn in buttons:
        try:
            if float(btn['text']) == correct_answer:
                btn.config(bg="green")
            elif btn == buttons[idx]:
                btn.config(bg="red")
        except ValueError:
            continue  # Если это не число, пропускаем

# Функция игры без ответов
def start_game_without_answers(selected_class, topic):
    clear_window()

    # Индекс текущего примера
    global current_example_index
    current_example_index = 0

    # Функция для показа следующего примера
    def show_next_example():
        global current_example_index
        custom_examples = data["custom_examples"].get(selected_class, {}).get(topic, [])

        if use_custom_examples.get() and custom_examples:
            if current_example_index < len(custom_examples):
                example_info = custom_examples[current_example_index]
                current_example_index += 1
                example = example_info['example']
            else:
                # Если все примеры учителя показаны, начнем генерировать новые примеры
                example, _ = generate_example(selected_class, topic)
        else:
            example, _ = generate_example(selected_class, topic)

        # Удаляем старый пример и создаем новый
        for widget in root.winfo_children():
            widget.destroy()

        # Выводим новый пример на экран
        label = tk.Label(root, text=f"Пример: {example}", font=("Arial", 24))
        label.pack(pady=20)

        # Кнопка для следующего примера
        next_example_button = tk.Button(root, text="Следующий пример", font=("Arial", 16),
                                        command=show_next_example)
        next_example_button.pack(pady=10)

        # Кнопка для возврата на предыдущий экран
        back_button = tk.Button(root, text="Назад", font=("Arial", 16),
                                command=lambda: select_mode_screen(selected_class, topic))
        back_button.pack(pady=20)

    # Изначально показываем первый пример
    show_next_example()

# Функция выбора класса
def start_game_screen():
    clear_window()
    label = tk.Label(root, text="Выберите класс", font=("Arial", 24))
    label.pack(pady=20)

    classes_frame = tk.Frame(root)
    classes_frame.pack()

    # Отображаем все классы
    for i, class_name in enumerate(data["classes"].keys()):
        class_button = tk.Button(classes_frame, text=class_name, font=("Arial", 16),
                                 command=lambda c=class_name: select_topic_screen(c))
        class_button.grid(row=i // 2, column=i % 2, padx=20, pady=10)

    manage_frame = tk.Frame(root)
    manage_frame.pack(pady=20)

    add_class_button = tk.Button(manage_frame, text="Добавить класс", font=("Arial", 16),
                                 command=lambda: manage_classes("Добавить"))
    add_class_button.grid(row=0, column=0, padx=10)

    delete_class_button = tk.Button(manage_frame, text="Удалить класс", font=("Arial", 16),
                                    command=lambda: manage_classes("Удалить"))
    delete_class_button.grid(row=0, column=1, padx=10)

    edit_class_button = tk.Button(manage_frame, text="Изменить класс", font=("Arial", 16),
                                  command=lambda: manage_classes("Изменить"))
    edit_class_button.grid(row=0, column=2, padx=10)

    back_button = tk.Button(root, text="Назад", font=("Arial", 16), command=main_menu)
    back_button.pack(pady=20)

# Функция главного меню
def main_menu():
    clear_window()
    label = tk.Label(root, text="Математическая игра", font=("Arial", 32))
    label.pack(pady=20)

    img = tk.PhotoImage(file="")
    img_label = tk.Label(root, image=img)
    img_label.image = img
    img_label.pack(pady=10)

    author_label = tk.Label(root, text="Автор: Гайков Максим", font=("Arial", 16))
    author_label.pack(pady=10)

    button_start = tk.Button(root, text="Начать", font=("Arial", 24), command=start_game_screen)
    button_start.pack(pady=20)

# Запуск программы
root = tk.Tk()
root.title("Математическая игра для учителей")
root.geometry("800x700")

main_menu()
root.mainloop()