import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Questions(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'questions'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    question_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    question = sqlalchemy.Column(sqlalchemy.String,nullable=False)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    answer_options = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    answer = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    owner_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    is_public = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False,default=False)



    def __repr__(self):
        return f'<questions> {self.question}'
