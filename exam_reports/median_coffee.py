from __future__ import annotations

from collections import defaultdict
from statistics import median
from typing import Any

from exam_reports.base import Report


class MedianCoffeeReport(Report):
    """Медиана coffee_spent по каждому студенту по всем переданным файлам; сортировка по убыванию."""

    name = "median-coffee"

    def build(self, rows: list[dict[str, str]]) -> tuple[list[str], list[list[Any]]]:
        by_student: dict[str, list[int]] = defaultdict(list)
        for row in rows:
            by_student[row["student"]].append(int(row["coffee_spent"]))
        pairs = [(student, median(values)) for student, values in by_student.items()]
        pairs.sort(key=lambda item: item[1], reverse=True)
        headers = ["student", "median_coffee"]
        table = [[student, med] for student, med in pairs]
        return headers, table
