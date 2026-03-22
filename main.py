from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tabulate import tabulate

from exam_reports.loader import load_csv_rows
from exam_reports.registry import get_report


def _configure_text_streams() -> None:
    """На Windows консоль часто не UTF-8; tabulate с кириллицей читается корректнее в utf-8."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8")
            except (OSError, ValueError, AttributeError):
                pass


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Отчёты по CSV с данными подготовки к экзаменам.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        metavar="PATH",
        help="Пути к одному или нескольким CSV-файлам",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Идентификатор отчёта (например median-coffee)",
    )
    return parser.parse_args(argv)


def ensure_files_exist(paths: list[str]) -> None:
    for raw in paths:
        p = Path(raw)
        if not p.is_file():
            print(f"Ошибка: файл не найден: {raw}", file=sys.stderr)
            sys.exit(1)


def run(argv: list[str] | None = None) -> int:
    _configure_text_streams()
    args = parse_args(argv)
    ensure_files_exist(args.files)
    try:
        report = get_report(args.report)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1
    rows = load_csv_rows(args.files)
    headers, table = report.build(rows)
    print(tabulate(table, headers=headers, tablefmt="grid"))
    return 0


def main() -> None:
    sys.exit(run())


if __name__ == "__main__":
    main()
