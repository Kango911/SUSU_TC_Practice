def main():
    print("=" * 60)
    print("🚀 УСЛОЖНЕННЫЕ ПРОГРАММЫ PYTHON")
    print("=" * 60)

    while True:
        print("\nВыберите программу для запуска:")
        print("1. 🏙️  Программа 'Города России'")
        print("2. ➕ Программа 'Математические примеры'")
        print("3. ❌ Выход")

        choice = input("\nВведите номер программы (1-3): ").strip()

        if choice == '1':
            from city_program import city_program
            city_program()
        elif choice == '2':
            from math_program import math_program
            math_program()
        elif choice == '3':
            print("\nСпасибо за использование программ!")
            print("📁 Исходный код доступен на моем GitHub: https://github.com/Kango911")
            break
        else:
            print("❌ Неверный выбор. Пожалуйста, введите 1, 2 или 3.")


if __name__ == "__main__":
    main()