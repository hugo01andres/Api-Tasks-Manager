from flask_restx import Resource, Namespace, fields


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

    ReadUser = api.model('ReadUser', {
        'id': fields.Integer(required=True, description='User id'),
        'name': fields.String(required=True, description='User name'),
        'username': fields.String(required=True, description='User username'),
        'email': fields.String(required=True, description='User email')
    })

    return CreateUserDto, UpdateUserDto, ReadUser
        