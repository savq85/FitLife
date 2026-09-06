import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')


while True:
    user_name = input("Введите ваше имя:")
    if not user_name:
        print("Введите имя")
    elif not user_name.isalpha():
        print("Имя должно состоять из букв")
    else:
        break


while True:
    try:
        user_age = int(input("Введите ваш возраст:"))
        if 0 <= user_age <= 100:
            break
    except ValueError:
        print("Пожалуйста, введите ваш возраст")


while True:
    try:
        user_weight = float(input("Введите ваш вес (например 100 кг):"))
        if 1 <= user_weight <= 200:
            break
    except ValueError:
        print("Пожалуйста, введите вас вес")


while True:
    try:
        user_height = float(input("Введите ваш рост (например 1.75):"))
        if 1 <= user_height <= 250:
            break
    except ValueError:
        print("Пожалуйста, введите ваш рост в метрах")


def calculate_bmi(user_weight, user_height):
    """Функция вызывает функцию"""
    if user_height <= 0:
        return None
    return user_weight / (user_height ** 2)


result_bmi = calculate_bmi(user_weight, user_height)


water_ml = user_weight * 30
water_l = water_ml / 1000


print(f"Отчет для пользователя: {user_name} ({user_age}) лет!")
print(f"Твой Индекс Массы Тела: {round(result_bmi, 1)}")
print(f"Рекомендуемая норма воды: {round(water_l, 2)} л. в день")
print("Расчет окончен. Будьте здоровы!")
