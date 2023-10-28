from app.Infraestructure.Repositories.UserRepository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_by_username(self, username):
        return self.user_repository.get_by_username(username)

    def get_by_id(self, id):
        return self.user_repository.get_by_id(id)

    def get_all(self):
        return self.user_repository.get_all()

    def create(self, user):
        return self.user_repository.add(user)

    def update(self, id, user):
        return self.user_repository.update(id,user)

    def delete(self, user):
        return self.user_repository.delete(user)