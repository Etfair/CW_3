from utils import get_data, filter_data, sort_data, format_data


def main():
    # Получение данных из файла
    data = get_data()

    # Фильтрация данных по статусу "EXECUTED"
    data = filter_data(data)

    # Сортировка данных на увеличение даты и возврат пяти последних операций
    data = sort_data(data)

    # Склеивание данных в требуемый шаблон
    data = format_data(data)

    for row in data:
        print(row)


if __name__ == '__main__':
    main()
