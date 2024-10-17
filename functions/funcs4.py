def process_order(*args, name, surname):
    print("Продукты:", *args)
    print("Информация:")
    print("name:", name)
    print("surname:", surname)

process_order('Пицца', 'Суши', 'Суши' , name='Райан', surname='Гослинг')