"""Заказы смены: загрузка из CSV и расчёты выручки по официантам."""

from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:
    """Читает заказы смены из CSV-файла и превращает строки в объекты Order.

    Args:
        path: путь к CSV-файлу с колонками waiter и kopeks.

    Returns:
        Список заказов в том порядке, в каком они записаны в файле.
    """
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """Суммирует выручку каждого официанта и сортирует их по убыванию.

    Args:
        orders: заказы смены, имена официантов уже приведены к одному виду.
        top: сколько лучших официантов вернуть; 0 — вернуть всех.

    Raises:
        ValueError: если список заказов пуст.

    Returns:
        Словарь «официант — выручка в копейках», от большей суммы к меньшей.
    """
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:
    """Упорядочивает заказы прямо в переданном списке: самые дорогие первыми."""
    orders.sort(key=lambda order: -order.kopeks)
