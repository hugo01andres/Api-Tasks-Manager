from app.Infraestructure.RepositoryBase import RepositoryBase
from app.app import db
from app.Models.User import User
from marshmallow import ValidationError

class UserRepository(RepositoryBase):
    def __init__(self):
        session = db.session
        super().__init__(User, session)

    def get_by_username(self, username):
        try:
            return self.model.query.filter_by(username=username).first()
        except Exception as e:
            raise ValidationError("Error al obtener el registro")