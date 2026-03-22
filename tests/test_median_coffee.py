from exam_reports.median_coffee import MedianCoffeeReport


def test_median_across_all_rows_sorted_descending() -> None:
    rows = [
        {"student": "B", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "10"},
        {"student": "A", "coffee_spent": "30"},
        {"student": "B", "coffee_spent": "200"},
        {"student": "B", "coffee_spent": "300"},
    ]
    headers, table = MedianCoffeeReport().build(rows)
    assert headers == ["student", "median_coffee"]
    # B: median [100,200,300] = 200; A: median [10,30] = 20
    assert table == [["B", 200], ["A", 20]]


def test_single_observation_median_is_that_value() -> None:
    rows = [{"student": "X", "coffee_spent": "42"}]
    _, table = MedianCoffeeReport().build(rows)
    assert table == [["X", 42]]


def test_even_count_median_average() -> None:
    rows = [
        {"student": "Y", "coffee_spent": "10"},
        {"student": "Y", "coffee_spent": "20"},
    ]
    _, table = MedianCoffeeReport().build(rows)
    assert table == [["Y", 15]]
