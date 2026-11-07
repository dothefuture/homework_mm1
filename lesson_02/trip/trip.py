# Учёт расходов в поездке. Один файл: и данные, и расчёты, и вывод на экран.
# Это стартовая точка домашней работы: вынести расчёты в отдельный модуль.
from rich import print

from calculator import calculate_average, calculate_total

EXPENSES = [
    {"day": 1, "category": "еда", "amount": 540},
    {"day": 1, "category": "транспорт", "amount": 260},
    {"day": 1, "category": "жильё", "amount": 1800},
    {"day": 2, "category": "еда", "amount": 720},
    {"day": 2, "category": "транспорт", "amount": 180},
    {"day": 2, "category": "жильё", "amount": 1800},
    {"day": 3, "category": "еда", "amount": 430},
    {"day": 3, "category": "транспорт", "amount": 95},
    {"day": 3, "category": "жильё", "amount": 1800},
    {"day": 3, "category": "еда", "amount": 275},
]


def format_report(expenses):
    total = calculate_total(expenses)
    average = calculate_average(expenses)
    lines = [
        "[bold green]ОТЧЁТ ПО ПОЕЗДКЕ[/bold green]",
        "-" * 32,
        f"записей: {len(expenses)}",
        f"всего потрачено: {total} ₽",
        f"средняя трата: {average:.2f} ₽",
    ]
    return "\n".join(lines)


def main():
    print(format_report(EXPENSES))


if __name__ == "__main__":
    main()
