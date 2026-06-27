# test_patch_example.py

from unittest.mock import Mock, patch

# --- Тестируемый код (обычно в другом файле) ---
import requests
from mypy.types import Any


def get_external_data(item_id: int) -> Any:
    # Эта функция делает реальный сетевой запрос
    print(
        f"\nВызов requests.get для {item_id}..."
    )  # Оставим print для демонстрации, что он НЕ выполнится в тесте
    response = requests.get(f"https://api.example.com/items/{item_id}")
    if response.status_code == 200:
        return response.json()
    return None


# --- Конец тестируемого кода ---

# Использование patch как декоратора


@patch("requests.get")  # Патчим requests.get в текущем модуле, где он используется
def test_get_external_data_with_decorator(mock_requests_get: Any) -> None:
    # Настраиваем мок, который будет передан в mock_requests_get
    print("\nЗапуск test_get_external_data_with_decorator")
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Test Item"}
    mock_requests_get.return_value = mock_response

    data = get_external_data(1)

    assert data == {"id": 1, "name": "Test Item"}
    mock_requests_get.assert_called_once_with("https://api.example.com/items/1")


# Использование patch как контекстного менеджера


def test_get_external_data_with_context_manager() -> None:
    print("\nЗапуск test_get_external_data_with_context_manager")
    with patch("requests.get") as mock_requests_get_cm:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 2, "name": "Test Item"}
        mock_requests_get_cm.return_value = mock_response

        data = get_external_data(2)

        assert data == {"id": 2, "name": "Test Item"}
        mock_requests_get_cm.assert_called_once_with("https://api.example.com/items/2")
