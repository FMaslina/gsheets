import pygsheets


def init(secret_path, sheet_name):      # Получение нужной таблицы
    gc = pygsheets.authorize(client_secret=secret_path)
    sh = gc.open(sheet_name)
    wks = sh.sheet1
    return wks


def get_all_table_data(wks):      # Получение всех данных с таблицы
    data_list = []
    for row in wks.get_all_values():
        if row[0] and row[0] != 'register':
            data_list.append(row[:10])
    return data_list


#def get_rows_ids(data):     # Получение id всех записей
    #ids = []
    #for row in data:
        #ids.append(row[2])
    #return ids


def get_row_data_by_id(data, id):      # Получение нужной записи по id
    for row in data:
        if row[2] == str(id):
            return row
    return 'Запись не найдена'


def update_row_data_by_id(wks, id, value_update):   # Обновление нужной записи по id
    data = wks.get_all_values()
    for i in range(len(data)):
        if str(id) in data[i]:
            wks.update_value(f'J{i+1}', value_update)


wks = init('client_secret.json', 'Test')
table_data = get_all_table_data(wks)
print(table_data)
#print(get_row_data_by_id(table_data, 2028))
update_row_data_by_id(wks, 202, 'test')
