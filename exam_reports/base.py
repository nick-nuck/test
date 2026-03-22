from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Report(ABC):
    """Базовый класс отчёта: одна реализация на значение --report."""

    name: str

    @abstractmethod
    def build(self, rows: list[dict[str, str]]) -> tuple[list[str], list[list[Any]]]:
        """Возвращает (заголовки колонок, строки таблицы для tabulate)."""

