# BankOperations
<font size="4"><span style="color: green">***это серверная часть виджета банковских операций***</font>

<font size="4">***1. <u>masks.py:</u>***</font>

<font size="3">**get_mask_card_number**(card_number: str) -> str:</font>
    - принимает на вход номер карты и возвращает ее маску
<font size="3">**get_mask_account**(card_number: str) -> str:</font>
    - принимает на вход номер карты и возвращает её краткую маску


<font size="4">***2. <u>widget.py:</u>***</font>

<font size="3">**mask_account_card**(card_info: str) -> str:</font>
    - Принимает информацию о карте или счёте. Возвращает замаскированную строку

<font size="3">**get_date**(date_string: str) -> str:</font>
    - Принимает строку с текущей датой и возвращает строку в формате 'ДД.ММ.ГГГГ'


<font size="4">***3. <u>processing.py:</u>***</font>

<font size="3">**filter_by_state**(input_dict_list: list, state: str = 'EXECUTED') -> list:</font>
    - Функция принимает на вход список словарей по банковским операциям и возвращает новый список,
      с выборкой тех, у которых ключ 'state' содержит переданное в функцию значение

<font size="3">**sort_by_date**(dict_list_input: list, descending_order: bool = True) -> list :</font>
    - Функция принимает на вход список словарей по банковским операциям и возвращает новый список, отсортированный в заданном вторым параметром порядке

<font size="4"><span style="color: green">***Все модули покрыты тестами***</font>


Coverage report: 100% 

{coverage.py v7.13.4}, created at 2026-03-18 20:13 +0500

[index.html](htmlcov/index.html)