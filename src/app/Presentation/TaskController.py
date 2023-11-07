from app.Services.TaskService import TaskService
from flask_restx import Resource, Namespace
from injector import inject
from app.Presentation.Resources.TaskResource import task_resource
from app.Security.TokenTools import token_required, g_tokens
from flask import g


api = Namespace('tasks', description='Task related operations')

CreateTaskDto, UpdateTaskDto, ReadTask = task_resource(api)

#parser_task_lists = api.parser()
#parser_task_lists.add_argument('task_id', type=int, help='Task id', help='Task id')

@api.route('/', strict_slashes=False)
class TaskListByUser(Resource):
    @inject
    def __init__(self,task_service : TaskService, **kwargs):
        self.task_service = task_service
        super().__init__(**kwargs)

    api.doc('Lists_tasks')
    #@api.expect(parser_task_lists)
    @api.marshal_list_with(ReadTask)
    @token_required
    @g_tokens
    def get(self):
        """List all tasks"""
        tasks = self.task_service.get_all_by_user_id(g.user_id)
        return tasks, 200

    @api.doc('Create_task')
    @api.expect(CreateTaskDto)
    @api.marshal_with(ReadTask)
    @token_required
    @g_tokens
    def post(self):
        """Create a new task"""
        data = api.payload.copy()
        data['user_id'] = g.user_id
        print(data)
        task = self.task_service.create(**data)
        return task, 201
    

@api.route('/<int:id>')
@api.param('id', 'The task identifier')
@api.response(404, 'Task not found')
class Task(Resource):
    @inject
    def __init__(self, **kwargs):
        self.task_service = TaskService()
        super().__init__(**kwargs)
    
    @api.doc('Get_task')
    @api.marshal_with(ReadTask)
    @token_required
    @g_tokens
    def get(self, id):
        """Fetch a task given its identifier"""
        task = self.task_service.get_by_id(id, g.user_id)
        if not task:
            api.abort(404)
        else:
            return task, 200
    
    @api.doc('Update_task')
    @api.expect(UpdateTaskDto)
    @token_required
    @g_tokens
    @api.marshal_with(ReadTask)
    def put(self, id):
        """Update a task given its identifier"""
        data = api.payload.copy()
        data['user_id'] = g.user_id
        print(data)
        task = self.task_service.update(id,**data)
        if not task:
            api.abort(404)
        else:
            return task, 200
    
    @api.doc('Delete_task')
    @api.marshal_with(ReadTask)
    @token_required
    @g_tokens
    def delete(self, id):
        """Delete a task given its identifier"""
        task = self.task_service.get_by_id(id, g.user_id)
        if not task:
            api.abort(404)
        else:
            self.task_service.delete(task)
            return task, 200