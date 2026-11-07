# Расчёты по расходам поездки: общая сумма и средняя трата.


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_average(expenses):
    if not expenses:
        raise ValueError("список расходов пуст")
    return calculate_total(expenses) / len(expenses)
