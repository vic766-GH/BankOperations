import pytest
from unittest.mock import patch, Mock
from src.trans_operations import source_select, get_variant, process_bank_operations


@pytest.mark.parametrize('file,list_dict,selected,answers,result',
    [
    ('','test_transactions_dict_empty',['EXECUTED', 'CANCELED', 'PENDING'],
    ['', ['EXECUTED', 'CANCELED', 'PENDING'], '', '', '', '', ''], 'test_transactions_dict_empty'),
    ('test_transactions', 'test_transactions_dict_json',['EXECUTED', 'CANCELED', 'PENDING'],
    ['1', ['EXECUTED', 'CANCELED', 'PENDING'], '', '', '', '', ''], 'test_transactions_dict_json'),
    ('test_transactions', 'test_transactions_dict_csv',['EXECUTED', 'CANCELED', 'PENDING'],
    ['2', ['EXECUTED', 'CANCELED', 'PENDING'], '', '', '', '', ''], 'test_transactions_dict_csv'),
    ('test_transactions', 'test_transactions_dict_xlsx',['EXECUTED', 'CANCELED', 'PENDING'],
    ['3', ['EXECUTED', 'CANCELED', 'PENDING'], '', '', '', '', ''], 'test_transactions_dict_xlsx')
    ])

@patch("trans_operations.get_variant")
def test_source_select(mock_get_variant, file, list_dict, selected : list[str],
              answers, result, request: pytest.FixtureRequest):

    l_dict = request.getfixturevalue(list_dict)
    res_dict = request.getfixturevalue(result)

    mock_response = Mock()
    mock_response.return_value = answers
    mock_get_variant.return_value = mock_response.return_value

    test_answer = source_select(file)

    assert test_answer == (selected, res_dict)
    mock_get_variant.assert_called()
    # mock_get_variant.assert_called_with(file)


@pytest.mark.parametrize('file,selected,answers',
 [
     ('test_transactions',
      ['1', 'EXECUTED', '', '', ''],
      ['1', ['EXECUTED'], '', '', '', '', '']),
     ('test_transactions',
      ['2', 'EXECUTED, CANCELED', '', '', ''],
      ['2', ['EXECUTED', 'CANCELED'], '', '', '', '', '']),
     ('test_transactions',
      ['3', 'EXECUTED, CANCELED, PENDING', '', '', ''],
      ['3', ['EXECUTED', 'CANCELED', 'PENDING'], '', '', '', '', ''])
 ])

@patch('builtins.input')
def test_get_variant(self, file,selected,answers):
    self.side_effect=selected
    result_get_variant = get_variant()
    assert result_get_variant == answers


@pytest.mark.parametrize('list_dict,selected,result',
    [
    ('test_transactions_dict_empty',['EXECUTED', 'CANCELED', 'PENDING'],
    {}),
    ('test_transactions_dict_csv', [],
    {}),
    ('test_transactions_dict_empty', [],
    {}),
    ('test_transactions_dict_csv',['EXECUTED', 'CANCELED', 'PENDING'],
    {'EXECUTED' : 10, 'CANCELED' : 3, 'PENDING' : 2}),
    ('test_transactions_dict_csv', ['EXECUTED', 'CANCELED'],
    {'EXECUTED': 10, 'CANCELED': 3}),
    ('test_transactions_dict_csv', ['EXECUTED'],
    {'EXECUTED': 10}),
    ('test_transactions_dict_csv', ['EXECUTED', 'PENDING'],
    {'EXECUTED': 10, 'PENDING': 2}),
    ])

def test_process_bank_operations(list_dict : list[dict], selected : list[str], result : dict,
                                 request: pytest.FixtureRequest):

    l_dict = request.getfixturevalue(list_dict)

    test_answer = process_bank_operations(l_dict, selected)
    assert test_answer == result
