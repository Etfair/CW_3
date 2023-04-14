import json
from datetime import datetime


def get_data():
    """
    Открытие файла операций
    :return: Полученные данные
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    """
    Фильтрация операций по статусу Выполнено
    :return: отфильтрованные данные
    """
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def sort_data(data):
    """
    Сортировка данных по увеличению
    :return: возвращает 5 последних операций
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def format_data(data):
    """
    Извлечение необходимых данных из операций
    """
    formatted_data = []
    for row in data:
        # Получение статуса операции Перевод организации или открытие вклада
        description = row['description']

        # Указывается тип счета на который производится пополнение/открытие
        sender_to = row['to'].split()

        # Указывается номер счета на который поступает пополнение/открытие
        sender_to_bill = sender_to.pop(-1)

        # Форматирование даты под запрашиваемый формат
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")

        # Указывается ** и последние 4 символа номера счета на который поступает пополнение/открытие
        sender_to_bill = f" **{sender_to_bill[-4:]}"

        # Если в операциях есть пункт "from"
        if "from" in row:
            from_arrow = "->"
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            sender_to_info = " ".join(sender_to)

        #  Если в операциях нет пункта "from"
        else:
            sender_info = "Новый счет"
            sender_bill = ""
            from_arrow = ""
            sender_to_info = ""

        # Получение суммы операции
        total = row['operationAmount']['amount']
        total = "".join(total)

        # Получение валюты
        currency = row['operationAmount']['currency']['name']
        currency = "".join(currency)

        formatted_data.append(f"""
{date} {description}
{sender_info} {sender_bill} {from_arrow} {sender_to_info} {sender_to_bill}
{total} {currency}\
        """)
    return formatted_data
