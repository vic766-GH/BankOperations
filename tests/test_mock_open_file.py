import csv
from unittest.mock import mock_open, patch


def parse_csv(filename: str) -> list[dict]:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        # Дальнейшая обработка данных
    return list(reader)


# class TestParseCSV(unittest.TestCase):
#     def test_parse_valid_csv(self):
#         mock_csv_content = "name,age,city\nAlice,30,New York\nBob,25,Los Angeles"
#         with patch("builtins.open", mock_open(read_data=mock_csv_content)) as mock_file:
#             result = parse_csv("test_file.csv")
#             self.assertEqual(result, [{'age': '30', 'city': 'New York', 'name': 'Alice'},
#  {'age': '25', 'city': 'Los Angeles', 'name': 'Bob'}])  # Проверка результата
#             assert result == [{'age': '30', 'city': 'New York', 'name': 'Alice'},
#                                       {'age': '25', 'city': 'Los Angeles', 'name': 'Bob'}]  # Проверка результата


def test_parse_valid_csv() -> None:
    mock_csv_content = "name,age,city\nAlice,30,New York\nBob,25,Los Angeles"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)):
        result = parse_csv("test_file.csv")
        assert result == [
            {"age": "30", "city": "New York", "name": "Alice"},
            {"age": "25", "city": "Los Angeles", "name": "Bob"},
        ]  # Проверка результата


@patch(
    "builtins.open",
    mock_open(read_data="name,age,city\nAlice,30,New York\nBob,25,Los Angeles"),
)
def test_parse_valid_csv1() -> None:

    result = parse_csv("test_file.csv")
    assert result == [
        {"age": "30", "city": "New York", "name": "Alice"},
        {"age": "25", "city": "Los Angeles", "name": "Bob"},
    ]  # Проверка результата
