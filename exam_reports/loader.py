from __future__ import annotations

import csv
from pathlib import Path


def load_csv_rows(paths: list[str | Path]) -> list[dict[str, str]]:
    """Читает все строки из переданных CSV; каждая строка — словарь по заголовкам."""
    rows: list[dict[str, str]] = []
    for path in paths:
        p = Path(path)
        with p.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    return rows
