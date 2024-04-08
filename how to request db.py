from pprint import pprint
import requests

pprint(requests.get('http://127.0.0.1:5050/api/questions').json())
# порт сервера: 5050
pprint(requests.post('http://127.0.0.1:5050/api/questions',
                     json={'question_id': 3, # использовать уникальное значение иначе возникает 422 ошибка:
                           # Question with id 'question_id' already in the database")
                           'question': 'testdouble', # вопрос который задаётся
                           'type': 'one_choice', # тип вопроса множественный/единственный ответ
                           'answer_options': '1,2,3,pineapple',# варианты ответов указанных через запятую
                           'answer': '1', # ответ/ответы указанные через запятую
                           'owner_id': 123456,# id создателя вопроса
                           'is_public': True}).text) # доступен ли всем вопрос
# в post обязательно указывать все параметры заисключением is_public по умолчанию is_public равен False

pprint(requests.get('http://127.0.0.1:5050/api/questions/3').json()) # запрос получение 3 вопроса
pprint(requests.delete('http://127.0.0.1:5050/api/questions/3').json()) # запрос удаления 3 вопроса
pprint(requests.get('http://127.0.0.1:5050/api/questions').json()) # вывод всех вопросов

