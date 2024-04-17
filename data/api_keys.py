import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Api_keys(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'api_keys'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String,nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    api_key = sqlalchemy.Column(sqlalchemy.String, nullable=False)