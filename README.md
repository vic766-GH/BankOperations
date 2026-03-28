# BankOperations
## <font size="4"><span style="color: green">***это серверная часть виджета банковских операций***</font>

### <u>Модули:</u>


#### <font size="4">***1. <u>masks.py:</u>***</font>

<font size="3">**get_mask_card_number**(card_number: str) -> str</font>
    - принимает на вход номер карты и возвращает ее маску
<font size="3">**get_mask_account**(card_number: str) -> str</font>
    - принимает на вход номер карты и возвращает её краткую маску


#### <font size="4">***2. <u>widget.py:</u>***</font>

<font size="3">**mask_account_card**(card_info: str) -> str</font>
    - Принимает информацию о карте или счёте. Возвращает замаскированную строку

<font size="3">**get_date**(date_string: str) -> str</font>
    - Принимает строку с текущей датой и возвращает строку в формате 'ДД.ММ.ГГГГ'


#### <font size="4">***3. <u>processing.py:</u>***</font>

<font size="3">**filter_by_state**(input_dict_list: list, state: str = 'EXECUTED') -> list</font>
    - Принимает на вход список словарей по банковским операциям и возвращает новый список,
      с выборкой тех, у которых ключ 'state' содержит переданное в функцию значение

<font size="3">**sort_by_date**(dict_list_input: list, descending_order: bool = True) -> list</font>
    - Принимает на вход список словарей по банковским операциям и возвращает новый список,
отсортированный в заданном вторым параметром порядке


#### <font size="4">***4. <u>generators.py:</u>***</font>

<font size="3">**filter_by_currency**(list_of_dicts: list, currency: str) -> Generator[dict, None,
None]:</font>
    - Принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной

<font size="3">**transaction_descriptions**(list_of_dicts: list) -> Generator[str, None, None]:</font>
    - Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди

<font size="3">**card_number_generator**(first_num: int, last_num: int) -> Generator[str, None,
</font>Any]:</font>
     - Принимает начальное и конечное значения и выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера
    карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999

### <font size="4"><span style="color: green">***Тестирование***</font>

#### <font size="4">***1. <u>test_masks.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**masks.py**

<font size="3">**get_mask_card_number**(card_number: str) -> str</font>
    - Функция принимает на вход номер карты и возвращает ее маску

<font size="3">**get_mask_account**card_account: str) -> str</font> - Функция принимает на вход номер карты и возвращает её краткую маску

#### <font size="4">***2. <u>test_widget.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**widget.py** с применением параметризации

<font size="3">**mask_account_card**(card_info: str) -> str</font> - Функция принимает информацию о карте или счёте. Возвращает замаскированную строку

<font size="3">**get_date**(date_string: str) -> str</font> - Функция принимает строку с текущей датой и возвращает строку в формате 'ДД.ММ.ГГГГ'

#### <font size="4">***3. <u>test_processing.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**processing.py**
с применением параметризации. Дополнительно используются фикстуры из модуля <font size="3">
***conftest.py***</font>

<font size="3">**filter_by_state**(input_dict_list: list, state: str = "EXECUTED") -> list</font>
    - Функция принимает на вход список словарей по банковским операциям и возвращает
    новый список, с выборкой тех, у которых ключ 'state' содержит переданное в функцию значение

<font size="3">**sort_by_date**(dict_list_input: list, descending_order: bool = True) -> list</font>
    - Функция принимает на вход список словарей по банковским операциям и возвращает новый список,
отсортированный в заданном вторым параметром порядке




