import requests


print(1,requests.post('http://127.0.0.1:5050/getapikey',
                     json={'login': '123', 'password': '321'}).json())#Создание API ключа (в БД нет пользователя)
print(2,requests.post('http://127.0.0.1:5050/getapikey',
                     json={'login': '123', 'password': '321'}).json())#Создание API ключа (в БД пользователь - ошибка)
print(3,requests.get('http://127.0.0.1:5050/getapikey',
                     json={'login': '321', 'password': '321'}).json())#Запрос API ключа (неправильный неправильный логин - ошибка)
print(4,requests.get('http://127.0.0.1:5050/getapikey',
                     json={'login': '123', 'password': '323'}).json())#Запрос API ключа (неправильный неправильный пароль - ошибка)
print(5,requests.get('http://127.0.0.1:5050/getapikey',
                    json={'login': '123', 'password': '321'}).json())#Запрос API ключа
print(6,requests.delete('http://127.0.0.1:5050/getapikey',
                     json={'login': '123', 'password': '321'}).json())#Удаление API ключа (ошибки аналогичны get запрсу) при удалении ключа удаляются и все вопросы приязанные к этому API ключу



# Пример запроса ключа и его использование
requests.post('http://127.0.0.1:5050/getapikey',
                     json={'login': '123', 'password': '321'}).json()
API_key = requests.get('http://127.0.0.1:5050/getapikey',
                     json={'login': '123', 'password': '321'}).json()['api_key']

# порт сервера: 5050


print(7,requests.post(f'http://127.0.0.1:5050/{API_key}/questions',
                     json={'question_id': 3, # использовать уникальное значение(random.randint()) иначе возникает 422 ошибка:
                           # Question with id 'question_id' already in the database")
                           'question': 'testdouble', # вопрос который задаётся
                           'type': 'one_choice', # тип вопроса множественный/единственный ответ
                           'answer_options': '1,2,3,pineapple',# варианты ответов указанных через запятую
                           'answer': '1', # ответ/ответы указанные через запятую
                           'owner_id': 123456,# id создателя вопроса
                           'is_public': True}).json()) # доступен ли всем вопрос
# в post обязательно указывать все параметры заисключением is_public (по умолчанию is_public равен False)


print(8,requests.get(f'http://127.0.0.1:5050/{API_key}/questions').json()) # вывод всех вопросов
print(9,requests.get(f'http://127.0.0.1:5050/{API_key}/questions/3').json()) # запрос получение 3 вопроса (получение вопроса по id)
print(10,requests.delete(f'http://127.0.0.1:5050/{API_key}/questions/3').json()) # запрос удаления 3 вопроса (удаление вопроса по id)
print(11,requests.get(f'http://127.0.0.1:5050/{API_key}/questions').json()) # вывод всех вопросов



# Очистка бд от демонстрационного аккаунта

requests.delete('http://127.0.0.1:5050/getapikey',
                     json={'login': '123', 'password': '321'}).json()