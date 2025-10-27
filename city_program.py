import json
import os


class CityManager:
    def __init__(self, filename='cities.json'):
        self.filename = filename
        self.cities = self.load_cities()

    def load_cities(self):
        """Загрузка списка городов из файла"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Начальный список крупных городов России
            initial_cities = [
                "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
                "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону",
                "Уфа", "Красноярск", "Воронеж", "Пермь", "Волгоград"
            ]
            self.save_cities(initial_cities)
            return initial_cities

    def save_cities(self, cities=None):
        """Сохранение списка городов в файл"""
        if cities is None:
            cities = self.cities
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(cities, f, ensure_ascii=False, indent=2)

    def find_similar_city(self, user_input):
        """Поиск похожих городов"""
        similar = []
        user_input_lower = user_input.lower()

        for city in self.cities:
            city_lower = city.lower()
            # Проверяем различные варианты схожести
            if (user_input_lower in city_lower or
                    city_lower in user_input_lower or
                    self.levenshtein_distance(user_input_lower, city_lower) <= 2):
                similar.append(city)

        return similar

    def levenshtein_distance(self, s1, s2):
        """Расстояние Левенштейна для поиска похожих названий"""
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def add_city(self, city):
        """Добавление нового города"""
        if city not in self.cities:
            self.cities.append(city)
            self.save_cities()
            return True
        return False


def city_program(user_name=""):
    manager = CityManager()

    print("\n" + "=" * 50)
    print("🏙️  ПРОГРАММА: ГОРОДА РОССИИ")
    if user_name:
        print(f"👤 Пользователь: {user_name}")
    print("=" * 50)
    print(f"📊 В базе данных: {len(manager.cities)} городов")
    print("=" * 50)

    while True:
        user_city = input("\nВ каком городе Вы живёте? ").strip()

        if not user_city:
            print("❌ Пожалуйста, введите название города.")
            continue

        # Проверяем, есть ли город в списке
        found_city = None
        for city in manager.cities:
            if user_city.lower() == city.lower():
                found_city = city
                break

        if found_city:
            print(f"\n🎉 {found_city} - хороший город!")

            # Сохраняем статистику
            save_city_interaction(user_city, True)
            break
        else:
            print(f"\n❌ Город '{user_city}' не найден в списке.")

            # Сохраняем статистику
            save_city_interaction(user_city, False)

            # Ищем похожие города
            similar_cities = manager.find_similar_city(user_city)

            if similar_cities:
                print("🔍 Возможно, вы имели в виду один из этих городов:")
                for i, city in enumerate(similar_cities, 1):
                    print(f"   {i}. {city}")

                choice = input("\nВыберите номер города или нажмите Enter для продолжения: ")
                if choice.isdigit() and 1 <= int(choice) <= len(similar_cities):
                    selected_city = similar_cities[int(choice) - 1]
                    print(f"\n🎉 {selected_city} - хороший город!")
                    break

            # Предлагаем добавить город
            add_choice = input("\nХотите добавить этот город в список? (да/нет): ").lower()
            if add_choice in ['да', 'д', 'yes', 'y']:
                if manager.add_city(user_city):
                    print(f"✅ Город '{user_city}' успешно добавлен в список!")
                    print(f"\n🎉 {user_city} - хороший город!")
                    break
                else:
                    print("⚠️ Этот город уже есть в списке!")
            else:
                print("🔄 Попробуйте ввести другой город.")


def save_city_interaction(city_name, found):
    """Сохранение статистики по городам"""
    stats = {
        "searches": 0,
        "found": 0,
        "not_found": 0
    }

    # Загружаем существующую статистику
    if os.path.exists('city_stats.json'):
        try:
            with open('city_stats.json', 'r', encoding='utf-8') as f:
                stats = json.load(f)
        except:
            pass

    # Обновляем статистику
    stats["searches"] = stats.get("searches", 0) + 1
    if found:
        stats["found"] = stats.get("found", 0) + 1
    else:
        stats["not_found"] = stats.get("not_found", 0) + 1

    # Сохраняем обновленную статистику
    with open('city_stats.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    city_program()