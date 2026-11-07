# trip — отчёт о расходах в поездке

Программа считает, сколько всего потрачено в поездке и какая средняя трата,
и печатает короткий отчёт.

## Запуск

Windows (PowerShell):

```text
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
py trip.py
```

macOS / Linux:

```text
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 trip.py
```

## Что печатает

```text
ОТЧЁТ ПО ПОЕЗДКЕ
--------------------------------
записей: 10
всего потрачено: 7900 ₽
средняя трата: 790.00 ₽
```

Заголовок выводится зелёным жирным шрифтом через библиотеку Rich.

## Файлы

- `trip.py` — данные о расходах, сборка и печать отчёта;
- `calculator.py` — расчёты: общая сумма и средняя трата;
- `requirements.txt` — зависимости (Rich).
