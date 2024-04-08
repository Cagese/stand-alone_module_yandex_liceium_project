from flask import Flask
from flask_restful import Api

from data import questions_resources, db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'database_api_key'
api = Api(app)


def main():
    db_session.global_init("db/api_database.sqlite")
    api.add_resource(questions_resources.QuestionsListResource, '/api/questions')  # для списка объектов
    api.add_resource(questions_resources.QuestionsResource, '/api/questions/<int:question_id>')  # для одного объекта
    app.run(port=5050)


if __name__ == '__main__':
    main()
