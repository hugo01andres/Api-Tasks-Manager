from app.app import db
from app.Infraestructure.RepositoryBase import RepositoryBase
from app.Models.Task import Task
from marshmallow import ValidationError

class TaskRepository(RepositoryBase):
    def __init__(self):
        session = db.session
        super().__init__(Task, session)

    def get_by_name(self, name):
        try:
            return self.model.query.filter_by(name=name).first()
        except Exception as e:
            raise ValidationError("Error al obtener el registro")