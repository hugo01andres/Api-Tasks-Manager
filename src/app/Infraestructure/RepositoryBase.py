from marshmallow import ValidationError


class RepositoryBase:
    def __init__(self, model, session):
        self.model = model
        self.session = session

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
            self.session.add(entity)
            self.session.commit()
        except Exception as e:
            print(f"Error: {e}")
            raise ValidationError("Error al add new record")
        
    def update(self, entity):
        try:
            self.session.merge(entity)
            self.session.commit()
        except Exception as e:
            raise ValidationError("Error to update record")
        
    def delete(self, entity):
        try:
            self.session.delete(entity)
            self.session.commit()
        except Exception as e:
            raise ValidationError("Error to delete record")
