# Практикум «Младший разработчик: первая неделя»

МДК.01.01 · аннотации типов и окружение проекта

- Студент: Сдобников Андрей
- Группа: РПО-2
- Сдано: 08.10.2026, 20:26:31

## Рецензия

| Письмо | Результат | Баллы |
|---|---|---|
| Письмо 1 · рабочее место | 18 из 18 | 2 / 2 |
| Письмо 2 · подписи по заявкам | 6 из 10 | 2 / 4 |
| Письмо 3 · вызовы и подпись | 40 из 40 | 2 / 2 |
| Письмо 4 · подпись вручную | 4 из 4 | 2 / 2 |
| **Итого** | | **8 / 10 · хорошо** |

- Рабочее место: все ответы верны.
- Подписи по заявкам: не решены заявки 3, 4, 8, 10. Повторите: словари и кортежи в аннотациях (глава 4.2, §2); порядок параметров со значением по умолчанию (глава 4.1, §3); запись X | None и объединение int | str (глава 4.2, §4–5); -> None у функции без результата (глава 4.2, §1).
- Вызовы и подпись: все строки разложены верно.
- Подпись вручную: все подписи верны.

## Письмо 1. Рабочее место

### Порядок команд — верно

1. `Распаковать архив и открыть папку проекта в VS Code: File → Open Folder, затем Terminal → New Terminal`
2. `python -m venv .venv`
3. `Активировать окружение: .venv\Scripts\activate в Windows или source .venv/bin/activate в macOS и Linux`
4. `python -m pip install -r requirements.txt`
5. `python main.py`

### Первый коммит — верно 10 из 10

| Файл | Ваш ответ | Верно |
|---|---|---|
| `main.py` | в репозиторий | ✓ |
| `app/calculator.py` | в репозиторий | ✓ |
| `tests/test_calculator.py` | в репозиторий | ✓ |
| `requirements.txt` | в репозиторий | ✓ |
| `README.md` | в репозиторий | ✓ |
| `.gitignore` | в репозиторий | ✓ |
| `.venv/` | на компьютере | ✓ |
| `__pycache__/` | на компьютере | ✓ |
| `app/__pycache__/calculator.cpython-312.pyc` | на компьютере | ✓ |
| `.env` | на компьютере | ✓ |

### Вопросы из чата — верно 7 из 7

| Вопрос | Ваша причина | Верно |
|---|---|---|
| 1. Денис | Пакет установлен в другой Python, не в окружение проекта | ✓ |
| 2. Лиза | Окружение не активно в этом терминале | ✓ |
| 3. Ксюша | Зависимости проекта не записаны в requirements.txt | ✓ |
| 4. Глеб | Нет правил .gitignore для окружения и кэша | ✓ |
| 5. Марат | Список зависимостей снят не в окружении проекта | ✓ |
| 6. Оля | VS Code использует другой интерпретатор, не из .venv | ✓ |
| 7. Тимур | Окружение перенесено с другого компьютера | ✓ |

## Письмо 2. Подписи по заявкам

### 1. Колледж «Северный» · электронный журнал — верно

```python
def average_grade(grades: list[int]) -> float:
```

### 2. Колледж «Северный» · посещаемость — верно

```python
def count_absences(marks: list[str]) -> int:
```

### 3. Кофейня «Зерно» · касса — неверно

```python
def order_total(discount: int = 0, items: dict[str, int]) -> int:
```

### 4. Кофейня «Зерно» · постоянные гости — неверно

```python
def find_guest_phone(name: str, guests: dict[str, str]) -> str:
```

### 5. Фитнес-клуб «Пульс» · абонементы — верно

```python
def is_membership_active(today: date, end_date: date) -> bool:
```

### 6. Книжный магазин «Переплёт» · склад — верно

```python
def parse_quantity(value: int | str) -> int:
```

### 7. Курьерская служба «Квартал» · отчёт за день — верно

```python
def distance_bounds(distances: list[float]) -> tuple[float, float]:
```

### 8. Кофейня «Зерно» · печать чека — неверно

```python
def print_receipt(width: int = 32, lines: list[str]) -> None:
```

### 9. Колледж «Северный» · ведомость группы — верно

```python
def average_by_student(journal: dict[str, list[int]]) -> dict[str, float]:
```

### 10. Фитнес-клуб «Пульс» · карта клиента — неверно

```python
def format_name(first_name: str, last_name: str, middle_name=None) -> str:
```

## Письмо 3. Вызовы и подпись

| Подпись | Верно |
|---|---|
| `def average_grade(grades: list[int]) -> float:` | 8 из 8 |
| `def find_guest_phone(guests: dict[str, str], name: str) -> str \| None:` | 8 из 8 |
| `def format_name(last_name: str, first_name: str, middle_name: str \| None = None) -> str:` | 8 из 8 |
| `def parse_quantity(value: int \| str) -> int:` | 8 из 8 |
| `def print_receipt(lines: list[str], width: int = 32) -> None:` | 8 из 8 |

## Письмо 4. Подпись вручную

### 1. Колледж «Северный» · лучший студент — верно

```python
def best_student(averages: dict[str, float]) -> str | None:
```

### 2. Фитнес-клуб «Пульс» · бонусы — верно

```python
def add_bonus(balance: int, visits: int, is_vip: bool = False) -> int:
```

### 3. Курьерская служба «Квартал» · адреса — верно

```python
def split_address(address: str) -> tuple[str, str]:
```

### 4. Книжный магазин «Переплёт» · авторы — верно

```python
def unique_authors(books: list[tuple[str, str]]) -> set[str]:
```
