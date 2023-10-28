from flask_restx import Resource, Namespace, fields


class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'

def user_resource(api):
    CreateUserDto = api.model('CreateUserDto', {
        'name': fields.String(required=True, description='User name'),
        'username': fields.String(required=True, description='User username'),
        'email': fields.String(required=True, description='User email'),
        'password': fields.String(required=True, description='User password')
    })

    UpdateUserDto = api.model('UpdateUserDto', {
        'name': fields.String(required=False, description='User name'),
        'username': fields.String(required=False, description='User username'),
        'email': fields.String(required=False, description='User email'),
        'password': fields.String(required=False, description='User password')
    })
    Task = api.model('Task', {
        'name': fields.String(required=True, description='Task name'),
    })

    ReadUser = api.model('ReadUser', {
        'id': fields.Integer(required=True, description='User id'),
        'name': fields.String(required=True, description='User name'),
        'username': fields.String(required=True, description='User username'),
        'email': fields.String(required=True, description='User email'),
        'tasks': fields.List(fields.Nested(Task), description='User tasks', allow_null=True)
    })

    return CreateUserDto, UpdateUserDto, ReadUser
        