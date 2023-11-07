from flask_restx import ValidationError
from app.Infraestructure.Repositories.TaskRepository import TaskRepository
from app.Models.Task import Task
from colorama import Fore, Style

class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    def get_by_name(self, name):
        return self.task_repository.get_by_name(name)

    def get_by_id(self, id, user_id):
        if self.task_repository.get_by_id(id).user_id != user_id:
            raise ValidationError(f"{Fore.YELLOW}Trying to get a task that is not yours{Style.RESET_ALL}")
        return self.task_repository.get_by_id(id)

    def get_all(self):
        return self.task_repository.get_all()
    
    def get_all_by_user_id(self, user_id):
        return self.task_repository.get_all_by_user_id(user_id)

    def create(self,name, user_id):
        task = Task(name=name, user_id=user_id)
        self.task_repository.add(task)
        return task

    def update(self, id, name, user_id):
        task = self.update_register(id,user_id,name)
        print(task.id, task.name)
        self.task_repository.update(task)
        return task
    
    def update_register(self, id, user_id, name):
        if self.task_repository.get_by_id(id).user_id != user_id:
            raise ValidationError(f"{Fore.YELLOW}Trying to update a task that is not yours{Style.RESET_ALL}")
        task = self.task_repository.get_by_id(id)
        task.name = name
        return task

    def delete(self, task):
        return self.task_repository.delete(task)