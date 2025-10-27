import random
import operator


class MathTrainer:
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        self.operation_symbols = list(self.operations.keys())

    def generate_expression(self):
        """Генерация математического выражения"""
        # Генерируем три трехзначных числа
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
        num3 = random.randint(100, 999)

        # Выбираем две случайные операции
        op1 = random.choice(self.operation_symbols)
        op2 = random.choice(self.operation_symbols)

        # Создаем выражение
        expression = f"({num1} {op1} {num2}) {op2} {num3}"

        # Вычисляем результат
        try:
            # Вычисляем первую операцию
            first_result = self.operations[op1](num1, num2)
            # Вычисляем вторую операцию
            final_result = self.operations[op2](first_result, num3)

            # Проверяем на деление на ноль и целочисленность
            if final_result == float('inf') or final_result == float('-inf'):
                return self.generate_expression()

            return expression, round(final_result, 2)

        except ZeroDivisionError:
            return self.generate_expression()

    def check_answer(self, user_answer, correct_answer):
        """Проверка ответа с учетом погрешности"""
        try:
            user_float = float(user_answer)
            return abs(user_float - correct_answer) < 0.01
        except ValueError:
            return False


def math_program():
    trainer = MathTrainer()

    print("=" * 50)
    print("ПРОГРАММА: МАТЕМАТИЧЕСКИЕ ПРИМЕРЫ")
    print("=" * 50)
    print("Решите примеры с трехзначными числами!")
    print("Вводите ответы с точностью до двух знаков после запятой")
    print("=" * 50)

    score = 0
    total_questions = 5

    for i in range(total_questions):
        print(f"\nВопрос {i + 1}/{total_questions}:")

        expression, correct_answer = trainer.generate_expression()
        print(f"Вычислите: {expression}")

        user_answer = input("Ваш ответ: ").strip().replace(',', '.')

        if trainer.check_answer(user_answer, correct_answer):
            print("✅ Правильно!")
            score += 1
        else:
            print(f"❌ Неправильно. Правильный ответ: {correct_answer}")

    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ:")
    print(f"Правильных ответов: {score}/{total_questions}")
    print(f"Процент правильных ответов: {score / total_questions * 100:.1f}%")

    if score == total_questions:
        print("🎉 Отличный результат! Вы математический гений!")
    elif score >= total_questions * 0.7:
        print("👍 Хороший результат!")
    elif score >= total_questions * 0.5:
        print("😊 Неплохо, но можно лучше!")
    else:
        print("💪 Продолжайте тренироваться!")


if __name__ == "__main__":
    math_program()