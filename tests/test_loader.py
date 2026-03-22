from exam_reports.loader import load_csv_rows


def test_load_merges_multiple_files(tmp_path) -> None:
    a = tmp_path / "a.csv"
    b = tmp_path / "b.csv"
    a.write_text(
        "student,date,coffee_spent\n"
        "S1,2024-01-01,1\n",
        encoding="utf-8",
    )
    b.write_text(
        "student,date,coffee_spent\n"
        "S2,2024-01-02,2\n",
        encoding="utf-8",
    )
    rows = load_csv_rows([str(a), str(b)])
    assert len(rows) == 2
    assert rows[0]["student"] == "S1" and rows[1]["student"] == "S2"
