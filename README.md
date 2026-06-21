# BankOperations
## <font size="4"><span style="color: green">***это серверная часть виджета банковских операций***</font>

### <u>Модули:</u>


#### <font size="4">***1. <u>masks.py:</u>***</font>

<font size="3">**get_mask_card_number**(card_number: str) -> str</font>
    - принимает на вход номер карты и возвращает ее маску.
<font size="3">**get_mask_account**(card_number: str) -> str</font>
    - принимает на вход номер карты и возвращает её краткую маску.


#### <font size="4">***2. <u>widget.py:</u>***</font>

<font size="3">**mask_account_card**(card_info: str) -> str</font>
    - Принимает информацию о карте или счёте. Возвращает замаскированную строку.

<font size="3">**get_date**(date_string: str) -> str</font>
    - Принимает строку с текущей датой и возвращает строку в формате 'ДД.ММ.ГГГГ'.


#### <font size="4">***3. <u>processing.py:</u>***</font>

<font size="3">**filter_by_state**(input_dict_list: list, state: str = 'EXECUTED') -> list</font>
    - Принимает на вход список словарей по банковским операциям и возвращает новый список,
      с выборкой тех, у которых ключ 'state' содержит переданное в функцию значение.

<font size="3">**sort_by_date**(dict_list_input: list, descending_order: bool = True) -> list</font>
    - Принимает на вход список словарей по банковским операциям и возвращает новый список,
отсортированный в заданном вторым параметром порядке.


#### <font size="4">***4. <u>generators.py:</u>***</font>

<font size="3">**filter_by_currency**(list_of_dicts: list, currency: str) -> Generator[dict, None,
None]:</font>
    - Принимает на вход список словарей, представляющих транзакции и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной.

<font size="3">**transaction_descriptions**(list_of_dicts: list) -> Generator[str, None, None]:</font>
    - Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

<font size="3">**card_number_generator**(first_num: int, last_num: int) -> Generator[str, None,
</font>Any]:</font>
     - Принимает начальное и конечное значения и выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера
    карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.


#### <font size="4">***5. <u>spiral_gen.py:</u>***</font>

<font size="3">**spiral_generator**(n: int = 2, fn: int = 1) -> Generator[tuple, None, None]:</font>
     Программа создания и заполнения спиральной квадратной матрицы любой размерности. Возвращает спиральную матрицу,
     заполненную от центра. Параметры вызова: n - размерность матрицы, fn - первоначальное значение числовой
     последовательности.


#### <font size="4">***6. <u>decorators.py:</u>***</font>

<font size="3">**log**(filename: str = "cons") -> Any:</font>
     декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор принимает необязательный аргумент <font size="3">
    **"filename"**</font>, который определяет, куда будут записываться логи: Если filename задан,
    логи записываются в указанный файл (расположен в текущем рабочем каталоге). Иначе логи выводятся
    в консоль.

#### <font size="4">***7. <u>utils.py:</u>***</font>

<font size="3">**get_operations**(path: str) -> list:</font>
    Функция, которая получает путь к файлу с данными о транзакциях и возвращает список словарей с транзакциями.

<font size="3">**transaction_to_rub**(transaction: dict) -> float:</font>
   Функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях. Если транзакция выполнялась
в иной, чем рубль валюте, выполняется конвертация по курсу на дату транзакции с использованием внешнего API (APILayer).

#### <font size="4">***8. <u>external_api:</u>***</font>

<font size="3">**convert_currency**(date: str, to_currency: str, from_currency: str, amount: str) -> float:</font>
    Функция, которая получает информацию о транзакции и возвращает сумму транзакции в целевой валюте после конвертации
    исходной валюты по курсу на заданную дату с использованием сервиса (APILayer).

#### <font size="4">***9. <u>read_transactions.py:</u>***</font>

<font size="3">**read_csv**(path_csv_file: str) -> list[dict]:</font>
    Функция чтения финансовых операций из файла типа 'csv'. В качестве аргумента принимает путь к файлу в виде 
    строки и возвращает список словарей прочитанных транзакций.

<font size="3">**read_xls**(path_xls_file: str) -> list[dict]:</font>
    Функция чтения финансовых операций из файла типа 'Excel'. В качестве аргумента принимает путь к файлу в виде 
    строки и возвращает список словарей прочитанных транзакций.

#### <font size="4">***10. <u>trans_operations.py:</u>***</font>
Модуль, обеспечивающий функционал взаимодействия с пользователем для выбора источника данных по транзакциям, 
дальнейшей обработки полученных транзакций и вывода в консоль результатов работы, где реальные данные маскируются 
особым, ранее определённым способом. Работа с модулем производится путём запуска основной программы в модуле
<font size="3">**main.py**</font> из корневого каталога проекта.

<font size="4">***<u>main***()</u></font><font size="3"> -> None:</font>
    Основная функция для вызова вспомогательных модулей взаимодействия с пользователем и вывода в консоль
    результатов выборки транзакций.

<font size="3">**source_select**(file_name: str) -> tuple[list, list[dict]]:</font>
    Функция выполняющая основной диалог с пользователем для выбора источника транзакций и вариантов его
    предварительной обработки (сортировка, выборка). Принимает в качестве аргумента путь и имя файла без расширения
    и возвращает список словарей транзакций, сформированный по требованиям пользователя.

<font size="3">**print_select**(result_list: list[dict], state_select: list) -> None:</font>
    Функция вывода в консоль результатов выборки транзакций. Принимает подготовленный список словарей транзакций
    и строку заданных категорий состояния.

<font size="3">**get_variant**() -> list:</font>
    Функция опроса пользователя и получения параметров обработки транзакций.

<font size="3">**process_bank_search**(operations_data: list[dict], state: str) -> list[dict]:</font>
    функция, принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании ('description') есть данная строка.

<font size="3">**process_bank_operations**(data: list[dict], categories: list) -> dict:</font>
    функцию принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории. Категории операций хранятся в поле 'description'.

<font size="3">**mask_source**(card_info: str) -> str:</font>
    Функция маскирования номера с помощью библиотеки 're'.

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

#### <font size="4">***7. <u>test_utils.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**utils.py**
с применением параметризации и Mock.

<font size="3">**test_get_operations**(path_to_file: str, get_dict: dict) -> None:</font> - Тест функции,
предназначенной для получения  список словарей с транзакциями из заданного json-файла;</font>

<font size="3">**transaction_to_rub**(transaction: dict) -> float:</font> - Тест функции,
предназначенной для получения суммы полученной транзакции в рублёвом эквиваленте.</font>

#### <font size="4">***8. <u>test_external_api.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**external_api.py**
с применением параметризации, Mock и patch.

<font size="3">**test_convert_currency**(operation_date: str, to_currency: str, from_currency: str,
amount: str, result_converted: float) -> None:</font> - Тест функции, для конвертации валют с реальным
обращением к API (APILayer);</font>

<font size="3">**test_convert_currency_mock**(mock_convert_currency: Any, operation_date: str,
    to_currency: str, from_currency: str, amount: str, result_converted: float, ) -> None:</font> - Тест
функции, предназначенной для конвертации валют с маскированием обращения к API через Mock.</font>

#### <font size="4">***9. <u>test_read_transactions.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">**read_transactions.py**
с применением фикстур, Mock и patch.

<font size="3">**test_read_csv_mock1**(transactions_fixture: list[dict]) -> None:</font> - Тест функции
read_csv() с использованием объекта Mock в декораторе patch. Таким образом, мокирукется реальное чтение
из файла с последующей нормальной работой объекта csv.DictReader</font>

<font size="3">**test_read_csv_mock2**(transactions_fixture: list[dict], csv_stream_fixture: str) -> None:
</font> - Тест функции read_csv() с использованием объекта Mock в качестве контекстного менеджера.
Таким образом, мокирукется реальное чтение из файла с последующей нормальной работой объекта csv.DictReader.

<font size="3">**test_read_exel_mock**(mock_read_excel: Any, transactions_fixture: list[dict]) -> None: 
</font> - Тест функции read_xls() с использованием объекта Mock в качестве контекстного менеджера. Таким образом,
    мокирукется реальное чтение из файла.

#### <font size="4">***10. <u>test_trans_operations.py:</u>***</font>
Выполняет тестирование функций модуля <font size="3">test_trans_operations.py</font>
с применением фикстур, Mock и patch.

<font size="3">**test_source_select**(mock_get_variant, file, list_dict, selected: list[str],
answers, result, request: pytest.FixtureRequest):</font>
    Тест функции source_select() с применением параметризации, мокирования функции <font size="3">get_variant()
</font> и фикстур из модуля <font size="3">***conftest.py***</font>.

<font size="3">**test_get_variant**(self, file, selected, answers):</font>
    Тест функции <font size="3">get_variant()</font> с применением параметризации и мокирования реального ввода 
пользователя.

<font size="3">**test_process_bank_operations**(list_dict: str, selected: list[str], result: dict,
    request: pytest.FixtureRequest):</font>
    Тест функции <font size="3">process_bank_operations()</font> с применением параметризации.
