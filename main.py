if __name__ == "__main__":

    from src.masks import get_mask_account, get_mask_card_number

    print("\nМодуль src.masks\n")

    print(get_mask_card_number("7000792289606361"))
    print("___ end of get_mask_account ___")
    print(get_mask_account("73654108430135874305"))
    print("___ end get_mask_card_number ___")
    print("___ end of src.masks ___")

    from src.widget import get_date, mask_account_card

    print("\nМодуль src.widget\n")

    input_data = (
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    )

    for input_string in input_data:
        print(mask_account_card(input_string))
    print("___ end mask_account_card ___")
    print(get_date("2024-03-11T02:26:18.671407"))
    print("___ end get_date ___")
    print("___ end of src.widget ___")

    from src.processing import filter_by_state, sort_by_date

    print("\nМодуль src.processing\n")

    in_list_dict = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    state = "EXECUTED"
    sort_by_descending_order = False

    print(sort_by_date(filter_by_state(in_list_dict, "CANCELED"), sort_by_descending_order))
    print("___ end sort_by_drate(filter_by_state) ___")
    print("___ end of src.processing ___")

    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

    print("\nМодуль src.generators\n")

    usd_transactions = filter_by_currency(transactions, "USD")

    for i in range(len(transactions)):
        try:
            print(f"{i + 1}. {next(usd_transactions)}", sep="\n")
        except StopIteration:
            pass
    print("___ end of filter_by_currency ___")

    descriptions = transaction_descriptions(transactions)
    for i in range(len(transactions)):
        try:
            print(f"{i + 1}. {next(descriptions)}", sep="\n")
        except StopIteration:
            pass
    print("___ end of transaction_descriptions ___")

    fn = 1
    ln = 5
    card_number = card_number_generator(fn, ln)
    for i in range(ln - fn + 1):
        try:
            print(f"{i + 1}. {next(card_number)}", sep="\n")
        except StopIteration:
            print("\n Начальный номер больше конечного")
    print("___ end of card_number_generator ___")
    print("___ end of src.generators ___")

    from src.spiral_gen import spiral_generator

    print("\nМодуль src.spiral_gen\n")

    mfn = 101
    mn = 5

    gen = spiral_generator(n=mn, fn=mfn)
    for i in range(mn * mn):
        matrix = next(gen)
    for j in range(mn):
        print(matrix[j])
    print("___ end of spiral_generator ___")
    print("___ end of src.spiral_gen ___")
