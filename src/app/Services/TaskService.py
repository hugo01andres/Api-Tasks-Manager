from app.Infraestructure.Repositories.TaskRepository import TaskRepository
from app.Models.Task import Task

class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    def get_by_name(self, name):
        return self.task_repository.get_by_name(name)

    def get_by_id(self, id):
        return self.task_repository.get_by_id(id)

    def get_all(self):
        return self.task_repository.get_all()

    def create(self,name, user_id):
        task = Task(name=name, user_id=user_id)
        self.task_repository.add(task)
        return task

    def update(self, id, task):
        return self.task_repository.update(id,task)

    def delete(self, task):
        return self.task_repository.delete(task)