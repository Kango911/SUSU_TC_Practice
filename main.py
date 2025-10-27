import json
import os


def get_user_info():
    """Получение информации о пользователе"""
    print("=" * 60)
    print("🎓 СИСТЕМА АВТОРИЗАЦИИ СТУДЕНТА")
    print("=" * 60)

    while True:
        name = input("Введите ваше ФИО: ").strip()
        if name:
            break
        print("❌ ФИО не может быть пустым. Пожалуйста, введите ваше имя.")

    while True:
        group = input("Введите вашу учебную группу: ").strip()
        if group:
            break
        print("❌ Группа не может быть пустой. Пожалуйста, введите вашу группу.")

    # Сохраняем информацию о пользователе
    user_data = {
        "name": name,
        "group": group,
        "login_count": 1
    }

    # Пытаемся загрузить историю логинов
    try:
        if os.path.exists('user_history.json'):
            with open('user_history.json', 'r', encoding='utf-8') as f:
                history = json.load(f)
                if history.get("name") == name and history.get("group") == group:
                    user_data["login_count"] = history.get("login_count", 0) + 1
    except:
        pass

    # Сохраняем текущую сессию
    with open('user_history.json', 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=2)

    return name, group


def show_welcome_message(name, group, login_count):
    """Показать приветственное сообщение"""
    print("\n" + "=" * 60)
    print(f"🎉 ДОБРО ПОЖАЛОВАТЬ, {name.upper()}!")
    print("=" * 60)
    print(f"📚 Учебная группа: {group}")
    print(f"🔢 Количество запусков программы: {login_count}")
    print("=" * 60)


def main():
    # Получаем информацию о пользователе
    name, group = get_user_info()

    # Загружаем счетчик логинов для приветствия
    login_count = 1
    try:
        if os.path.exists('user_history.json'):
            with open('user_history.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                login_count = data.get("login_count", 1)
    except:
        pass

    show_welcome_message(name, group, login_count)

    while True:
        print(f"\n{name}, выберите программу для запуска:")
        print("1. 🏙️  Программа 'Города России'")
        print("2. ➕ Программа 'Математические примеры'")
        print("3. 📊 Посмотреть мою статистику")
        print("4. ❌ Выход")

        choice = input("\nВведите номер программы (1-4): ").strip()

        if choice == '1':
            from city_program import city_program
            city_program(name)
        elif choice == '2':
            from math_program import math_program
            math_program(name)
        elif choice == '3':
            show_user_statistics(name, group)
        elif choice == '4':
            print(f"\nСпасибо за использование программ, {name}!")
            print("📁 Исходный код доступен на GitHub: https://github.com/Kango911")
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор. Пожалуйста, введите число от 1 до 4.")


def show_user_statistics(name, group):
    """Показать статистику пользователя"""
    print("\n" + "=" * 50)
    print("📊 ВАША СТАТИСТИКА")
    print("=" * 50)
    print(f"👤 ФИО: {name}")
    print(f"📚 Группа: {group}")

    # Статистика по городам
    cities_count = 0
    if os.path.exists('cities.json'):
        with open('cities.json', 'r', encoding='utf-8') as f:
            cities_data = json.load(f)
            cities_count = len(cities_data)

    print(f"🏙️  Городов в базе: {cities_count}")

    # Статистика по математике
    math_stats = {"total_questions": 0, "correct_answers": 0}
    if os.path.exists('math_stats.json'):
        try:
            with open('math_stats.json', 'r', encoding='utf-8') as f:
                math_stats = json.load(f)
        except:
            pass

    if math_stats["total_questions"] > 0:
        success_rate = (math_stats["correct_answers"] / math_stats["total_questions"]) * 100
        print(f"🧮 Решено математических примеров: {math_stats['total_questions']}")
        print(f"✅ Правильных ответов: {math_stats['correct_answers']}")
        print(f"📈 Успешность: {success_rate:.1f}%")
    else:
        print("🧮 Математические примеры: еще не решены")

    print("=" * 50)


if __name__ == "__main__":
    main()