from flask_restx import Resource, Namespace , fields


class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'


def task_resource(api):
    CreateTaskDto = api.model('CreateTaskDto', {
        'name': fields.String(required=True, description='Task name'),
    })

    UpdateTaskDto = api.model('UpdateTaskDto', {
        'name': fields.String(required=False, description='Task name'),
    })

    ReadTask = api.model('ReadTask', {
        'id': fields.Integer(required=True, description='Task id'),
        'name': fields.String(required=True, description='Task name'),
    })

    return CreateTaskDto, UpdateTaskDto, ReadTask