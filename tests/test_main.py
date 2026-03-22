import sys

import pytest

from main import ensure_files_exist, run


def test_run_success_prints_table(capsys, tmp_path) -> None:
    csv_path = tmp_path / "data.csv"
    csv_path.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "A,2024-06-01,10,8,1,ok,X\n"
        "A,2024-06-02,30,8,1,ok,X\n",
        encoding="utf-8",
    )
    code = run(["--files", str(csv_path), "--report", "median-coffee"])
    assert code == 0
    out = capsys.readouterr().out
    assert "student" in out
    assert "median_coffee" in out
    assert "A" in out
    assert "20" in out


def test_run_unknown_report(capsys, tmp_path) -> None:
    csv_path = tmp_path / "x.csv"
    csv_path.write_text("student,date,coffee_spent\nA,2024-01-01,1\n", encoding="utf-8")
    code = run(["--files", str(csv_path), "--report", "no-such-report"])
    assert code == 1
    err = capsys.readouterr().err
    assert "Неизвестный отчёт" in err or "unknown" in err.lower()


def test_run_missing_file(capsys, tmp_path) -> None:
    missing = tmp_path / "nope.csv"
    with pytest.raises(SystemExit) as exc:
        run(["--files", str(missing), "--report", "median-coffee"])
    assert exc.value.code == 1
    err = capsys.readouterr().err
    assert "не найден" in err or "not found" in err.lower()


def test_ensure_files_exist_exits(monkeypatch, capsys, tmp_path) -> None:
    bad = tmp_path / "missing.csv"

    def fake_exit(code: int) -> None:
        raise SystemExit(code)

    monkeypatch.setattr(sys, "exit", fake_exit)
    with pytest.raises(SystemExit) as exc:
        ensure_files_exist([str(bad)])
    assert exc.value.code == 1
