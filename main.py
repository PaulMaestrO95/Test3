from pprint import pprint

A = [
    {
        "balance": -10324.54,
        "currency": "RUB",
        "status": "NORM",
        "productType": "Тариф "
    },
    {
        "balance": 0,
        "currency": "EUR",
        "status": "CLBL",
        "productType": "Текущий счет"
    },
    {
        "balance": 0,
        "currency": "RUB",
        "status": "CLBL",
        "productType": "Тариф"
    },
    {
        "balance": 9424.63,
        "currency": "USD",
        "status": "NORM",
        "productType": "Текущий счет"
    },
    {
        "balance": 2345.23,
        "currency": "RUB",
        "status": "NORM",
        "productType": "Текущий счет"
    }
]

get_array = []

[get_array.append(i) for i in A if i.get("currency") == "RUB"]

# for i in A:
#     if i.get("currency") == "RUB":
#         get_array.append(i)

pprint(get_array)