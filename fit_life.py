import io
import sys


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')


MIN_AGE = 10
MAX_AGE = 100
MIN_WIEGHT = 10
MAX_WIEGHT = 200
MIN_HEIGHT = 1.00
MAX_HIEGHT = 3.00
WATER_ML_KG = 30
ML_IN_LITTER = 1000


while True:
    user_name = input("Введите ваше имя:").strip()
    if not user_name:
        print("Введите имя")
    elif not user_name.isalpha():
        print("Имя должно состоять из букв")
    else:
        break


while True:
    try:
        user_age = int(input("Введите ваш возраст:"))
        if MIN_AGE <= user_age <= MAX_AGE:
            break
    except ValueError:
        print("Пожалуйста, введите ваш возраст")


while True:
    try:
        user_weight = float(input("Введите ваш вес (например 100 кг):"))
        if MIN_WIEGHT <= user_weight <= MAX_WIEGHT:
            break
    except ValueError:
        print("Пожалуйста, введите вас вес")


while True:
    try:
        user_height = float(input("Введите ваш рост (например 1.75):"))
        if MIN_HEIGHT <= user_height <= MAX_HIEGHT:
            break
    except ValueError:
        print("Пожалуйста, введите ваш рост в метрах")


def calculate_bmi(user_weight, user_height):
    """Функция для расчета ИМТ"""
    return user_weight / (user_height ** 2)


result_bmi = calculate_bmi(user_weight, user_height)


water_ml = user_weight * WATER_ML_KG
water_l = water_ml / ML_IN_LITTER


print(f"Отчет для пользователя: {user_name} ({user_age}) лет!")
print(f"Твой Индекс Массы Тела: {round(result_bmi, 1)}")
print(f"Рекомендуемая норма воды: {round(water_l, 2)} л. в день")
print("Расчет окончен. Будьте здоровы!")
