import pytest

from unittest.mock import patch, Mock
from src.trans_operations import source_select, get_variant, get_user
#
@pytest.mark.parametrize('file,list_dict,selected,answers,result',
     [
         ('','test_transactions_dict_empty','EXECUTED, CANCELED, PENDING', ['', ['EXECUTED', 'CANCELED',
                                                                                  'PENDING'], '', '', '', '', ''], 'test_transactions_dict_empty'),
         ('data/test_transactions', 'test_transactions_dict_json','EXECUTED, CANCELED, PENDING',
          ['1', ['EXECUTED', 'CANCELED', 'PENDING'], '', '', '', '', ''], 'test_transactions_dict_json'),
         ('data/test_transactions', 'test_transactions_dict_csv','EXECUTED, CANCELED, PENDING',
          ['2', ['EXECUTED', 'CANCELED', 'PENDING'], '', '', '', '', ''], 'test_transactions_dict_csv'),
         ('data/test_transactions', 'test_transactions_dict_xlsx','EXECUTED, CANCELED, PENDING',
          ['3', ['EXECUTED', 'CANCELED', 'PENDING'], '', '', '', '', ''], 'test_transactions_dict_xlsx')
     ])


@patch("src.trans_operations.get_variant")
def test_main(mock_get_variant, file, list_dict, selected, answers, result, request: pytest.FixtureRequest):
#     #def test_main(file, list_dict, selected, result, request: pytest.FixtureRequest):
#def test_main(mock_get_variant, request: pytest.FixtureRequest):
    l_dict = request.getfixturevalue(list_dict)
    res_dict = request.getfixturevalue(result)

    mock_response = Mock()
    mock_response.return_value = answers
    mock_get_variant.return_value = mock_response.return_value

    test_answer = source_select(file)

    # assert test_answer == ['1', ['EXECUTED', 'CANCELED', 'PENDING'], '', '', '', '', '']
    # mock_get_variant.assert_called_once_with('data/test_transactions')
    assert test_answer == (['EXECUTED', 'CANCELED', 'PENDING'], res_dict)
    mock_get_variant.assert_called()
    mock_get_variant.assert_called_with(file)

