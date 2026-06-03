from pprint import pprint


def process_grades(records: list[str]) -> dict:
    """Parse grade records and return summary statistics."""
    valid_count = 0
    skipped = 0
    total_score = 0
    passed_names: set[str] = set()

    for record in records:
        if not isinstance(record, str) or ":" not in record:
            skipped += 1
            continue

        name, score_text = record.split(":", 1)
        name = name.strip()
        score_text = score_text.strip()

        if not name:
            skipped += 1
            continue

        try:
            score = int(score_text)
        except ValueError:
            skipped += 1
            continue

        if score < 0 or score > 100:
            skipped += 1
            continue

        valid_count += 1
        total_score += score

        if score >= 60:
            passed_names.add(name)

    average = round(total_score / valid_count, 1) if valid_count else 0.0

    return {
        "valid_count": valid_count,
        "average": average,
        "passed": sorted(passed_names),
        "skipped": skipped,
    }


if __name__ == "__main__":
    example_data = [
        "Иванов: 85",
        "Петров: 42",
        "Сидоров: abc",
        "Козлов: 90",
        ": 55",
        "Иванов: 70",
    ]

    edge_data = [
        "",
        "Без оценки:",
        "Некорректный: 101",
        "Еще некорректный: -1",
        "Нет двоеточия",
    ]

    assert process_grades(example_data) == {
        "valid_count": 4,
        "average": 71.8,
        "passed": ["Иванов", "Козлов"],
        "skipped": 2,
    }

    assert process_grades(edge_data) == {
        "valid_count": 0,
        "average": 0.0,
        "passed": [],
        "skipped": 5,
    }

    print("Example data:")
    pprint(process_grades(example_data), sort_dicts=False)

    print("\nOnly broken data:")
    pprint(process_grades(edge_data), sort_dicts=False)
