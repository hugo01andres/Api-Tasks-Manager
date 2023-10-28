from marshmallow import ValidationError


class RepositoryBase:
    def __init__(self, model, db):
        self.model = model
        self.db = db

    def get_all(self):
        try:
            return self.model.query.all()
        except Exception as e:
            raise ValidationError("Error al obtener los registros")
        
    def get_by_id(self, id):
        try:
            return self.model.query.get(id)
        except Exception as e:
            raise ValidationError("Error al obtener el registro")
        
    def add(self, entity):
        try:
            self.db.session.add(entity)
            self.db.session.commit()
        except Exception as e:
            raise ValidationError("Error al agregar el registro")
        
    def update(self, entity):
        try:
            self.db.session.merge(entity)
            self.db.session.commit()
        except Exception as e:
            raise ValidationError("Error al actualizar el registro")
        
    def delete(self, entity):
        try:
            self.db.session.delete(entity)
            self.db.session.commit()
        except Exception as e:
            raise ValidationError("Error al eliminar el registro")
