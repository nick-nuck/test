from __future__ import annotations

from typing import Type

from exam_reports.base import Report
from exam_reports.median_coffee import MedianCoffeeReport

REPORTS: dict[str, Type[Report]] = {
    MedianCoffeeReport.name: MedianCoffeeReport,
}


def get_report(name: str) -> Report:
    cls = REPORTS.get(name)
    if cls is None:
        raise ValueError(
            f"Неизвестный отчёт {name!r}. Доступные: {', '.join(sorted(REPORTS))}"
        )
    return cls()
