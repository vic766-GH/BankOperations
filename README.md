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


#### <font size="4">***5. <u>spiral_gen.py:</u>***</font>

<font size="3">**spiral_generator**(n: int = 2, fn: int = 1) -> Generator[tuple, None, None]:</font>
     Программа создания и заполнения спиральной квадратной матрицы любой размерности. Возвращает спиральную матрицу,
     заполненную от центра. Параметры вызова: n - размерность матрицы, fn - первоначальное значение числовой
     последовательности


#### <font size="4">***6. <u>decorators.py:</u>***</font>

<font size="3">**log**(filename: str = "cons") -> Any:</font>
     декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор принимает необязательный аргумент <font size="3">
    **"filename"**</font>, который определяет, куда будут записываться логи: Если filename задан,
    логи записываются в указанный файл (расположен в текущем рабочем каталоге). Иначе логи выводятся
    в консоль.

### <font size="4"><span style="color: green">***Тестирование***</font>

#### <font size="4">***1. <u>test_masks.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**masks.py**

<font size="3">**test_get_mask_card_number**(card_number: str) -> str</font>
    - Тест программы возврата маски номера карты (<font size="3"> 
    ***get_mask_card_number***</font>).

<font size="3">**test_get_mask_account**(card_account: str) -> str</font>
    - Тест программы возврата краткой маски номера карты(<font size="3">
    ***mask_account_card***</font>).

#### <font size="4">***2. <u>test_widget.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**widget.py** с применением параметризации

<font size="3">**test_mask_account_card**(card_info: str) -> str</font>
    - Тест программы возврата замаскированной строки(<font size="3">***mask_account_card***</font>).

<font size="3">**test_get_date**(date_string: str) -> str</font>
    - Тест программы возврата даты в виде строки формата 'ДД.ММ.ГГГГ'
    (<font size="3">***get_date***</font>).

#### <font size="4">***3. <u>test_processing.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**processing.py**
с применением параметризации. Дополнительно используются фикстуры из модуля <font size="3">
***conftest.py***</font>

<font size="3">**test_filter_by_state**(input_dict_list: list, state: str = "EXECUTED") -> list</font>
    - Тест программы возврата списка с выборкой операций, у которых ключ 'state' содержит
переданное в функцию значение(<font size="3">***filter_by_state***</font>).

<font size="3">**test_sort_by_date**(dict_list_input: list, descending_order: bool = True) ->
    list</font>
    - Тест программы возврата списка, отсортированного в заданном вторым параметром порядке
    (<font size="3">***sort_by_date***</font>).

#### <font size="4">***4. <u>test_generators.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**generators.py**
с применением параметризации. Дополнительно используются фикстуры из модуля <font size="3">
***conftest.py***</font>

<font size="3">**test_filter_by_currency**(list_of_dicts: list, currency: str) -> 
    Generator[dict, None, None]:</font>
    - Тест программы возврата транзакции, где валюта операции соответствует заданной(<font size="3">
    ***filter_by_currency***</font>).

<font size="3">**test_transaction_descriptions**(list_of_dicts: list) -> 
    Generator[str, None, None]:</font>
    - Тест программы возврата описания каждой операции по очереди(<font size="3">
    ***transaction_descriptions***</font>).

<font size="3">**test_card_number_generator**(first_num: int, last_num: int) ->
    Generator[str, None, None]:</font>
    - Тест программы генерации номеров карт(<font size="3">***card_number_generator***</font>).

#### <font size="4">***5. <u>test_spiral_gen.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**spiral_gen.py**
с применением параметризации. Дополнительно используются фикстуры из модуля <font size="3">
***conftest.py***</font>

<font size="3">**test_spiral_generator**</font>
        - Тест программы создания и заполнения спиральной квадратной матрицы
        любой размерности (<font size="3">***spiral_generator***</font>).


#### <font size="4">***6. <u>test_decorators.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**decorators.py**
с применением параметризации.

<font size="3">**test_decorator**(unit: str, num_1: Any, num_2: Any, result: Any, capsys: Any) ->
    Any:</font> - Тест декоратора с параметрами из модуля decorators.py, выполняющего логирование работы
функции. При тестировании из логов исключается дата и время. Остаётся только фиксация начала работы функции, 
результат работы и завершение работы функции <font size="3">***my_function_summ***(x: Any, y: Any) ->
Any:</font>).
