from scr.utils import sort_data, filter_data, format_data

def test_sort_data(test_data):
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572', '2017-08-26T10:50:58.294041']

def test_filter_data_exe(test_data):
    assert [x['state'] for x in filter_data(test_data)] == ['EXECUTED', 'EXECUTED', 'EXECUTED']

def test_over_data(test_data):
    assert [x for x in format_data(test_data)] == ['\n'
 '26.08.2017 Перевод организации\n'
 'Maestro 1596 83** **** 5199 -> Счет  **9589\n'
 '31957.58 руб.        ',
 '\n'
 '03.07.2019 Перевод организации\n'
 'MasterCard 7158 30** **** 6758 -> Счет  **5560\n'
 '8221.37 USD        ',
 '\n'
 '30.06.2018 Перевод организации\n'
 'Счет 7510 68** **** 6952 -> Счет  **6702\n'
 '9824.07 USD        ']



