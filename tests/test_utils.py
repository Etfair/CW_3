from scr.utils import sort_data, filter_data
from datetime import datetime

def test_sort_data(test_data):
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572', '2017-08-26T10:50:58.294041']

def test_filter_data_exe(test_data):
    assert [x['state'] for x in filter_data(test_data)] == ['EXECUTED', 'EXECUTED', 'EXECUTED']

def test_format_data(test_data):
    for row in test_data:
        format_data = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        assert format_data == '03.07.2019' or '30.06.2018' or '26.08.2017'

