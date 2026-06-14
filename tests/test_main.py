from unittest.mock import patch

@patch('builtins.input')
def test_my_function(self, mock_input):
    # Здесь можно настроить поведение мокового объекта
    mock_input.return_value = 'Пример ввода'
    result = my_function()
    self.assertEqual(result, 'Пример ввода')
@patch('builtins.input', side_effect=['First', 'Second', 'Third'])
def test_using_side_effect(self, mock_input):
    calling_1 = mock_input()
    calling_2 = mock_input()
    calling_3 = mock_input()
    self.assertTrue(calling_1 == 'First' and calling_2 == 'Second' and
                    calling_3 == 'Third')
