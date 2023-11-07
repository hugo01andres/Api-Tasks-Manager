from flask_restx import Resource, Namespace, fields


class NullableString(fields.String):
    __schema_type__ = ['string', 'null']
    __schema_example__ = 'nullable string'

def token_resource(api):
    GenerateToken = api.model('GenerateToken', {
        'username': fields.String(required=True, description='User username'),
        'password': fields.String(required=True, description='User password')
    })

    Token = api.model('Token', {
        'token': fields.String(description='Access token'),
    })

    return GenerateToken, Token