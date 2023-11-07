from app.Services.UserService import UserService
from flask_restx import Resource, Namespace
from injector import inject
from app.Presentation.Resources.UserResource import user_resource
from app.Security.TokenTools import token_required
from flask import g


api = Namespace('users', description='User related operations')

CreateUserDto, UpdateUserDto, ReadUser = user_resource(api)

#parser_user_lists = api.parser()
#parser_user_lists.add_argument('user_id', type=int, help='User id', help='User id')
@api.route('/', strict_slashes=False)
class UserList(Resource):
    @inject
    def __init__(self,user_service : UserService, **kwargs):
        self.user_service = user_service
        super().__init__(**kwargs)
    # FIXME: Implement roles per user so we can use this
    # api.doc('Lists_users')
    # #@api.expect(parser_user_lists)
    # @api.marshal_list_with(ReadUser)
    # @token_required
    # def get(self):
    #     """List all users"""
    #     users = self.user_service.get_all()
    #     return users, 200
    
    # @api.doc('Create_user')
    # @api.expect(CreateUserDto)
    # @api.marshal_with(ReadUser)
    # @token_required
    # def post(self):
    #     """Create a new user"""
    #     data = api.payload.copy() #Is what the post brings
    #     print(data)
    #     user = self.user_service.create(**data)
    #     return user, 201
    

@api.route('/<int:id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found')
class User(Resource):
    @inject
    def __init__(self, **kwargs):
        self.user_service = UserService()
        super().__init__(**kwargs)
    
    @api.doc('Get_user')
    @api.marshal_with(ReadUser)
    @token_required
    def get(self, id):
        """Fetch a user given its identifier"""
        user = self.user_service.get_by_id(id)
        if not user:
            api.abort(404)
        else:
            return user, 200
    
    @api.doc('Update_user')
    @api.expect(UpdateUserDto)
    @api.marshal_with(ReadUser)
    @token_required
    def put(self, id):
        """Update a user given its identifier"""
        data = api.payload
        if id == g.user_id:
            user = self.user_service.update(id, data)
        else:
            api.abort(404)
        if not user:
            api.abort(404)
        else:
            return user, 200
    
    @api.doc('Delete_user')
    @token_required
    @api.response(204, 'User deleted')
    def delete(self, id):
        """Delete a user"""
        if id == g.user_id:
            user = self.user_service.delete(id)
        else:
            api.abort(404)
        if not user:
            api.abort(404)
        else:
            return '', 204
    

@api.route('/register')
class Register(Resource):
    @inject
    def __init__(self, **kwargs):
        self.user_service = UserService()
        super().__init__(**kwargs)
    
    @api.doc('Register_user')
    @api.expect(CreateUserDto)
    def post(self):
        """Register a new user"""
        data = api.payload.copy()
        user = self.user_service.create(**data)
        return {"Registration": "Succesfully"}, 201
