from flask_restx import Namespace, Resource

api = Namespace("profile", description="profile related operations")

@api.route('/<int:id>')
@api.param('id', 'profile id')
class Profile(Resource):
    @api.doc('get_profile')
    def get(self, id):
        return {'id': id }