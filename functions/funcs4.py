def process_order(*args, **kwargs):
    print("Продукты:", *args)
    print("Информация:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

process_order('Пицца', 'Суши', 'Суши' , name='Райан', surname='Гослинг')