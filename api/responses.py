
class ResponseMessages():
    def create_entity(self, success):
        if success:
            response_message = {
                'success': True,
                'message': self + ' created successfully.'
            }
        else:
            response_message = {
                'success': False,
                'message': 'Error creating '+ self + '.'
            }
        return response_message

    def modify_entity(self, success, method):
        if method == 'GET':
            message = self + ' fetched successfully.'
        elif method == 'PUT':
            message = self + ' edited successfully.'
        elif method == 'DELETE':
            message = self + ' deleted successfully.'
        if success:
            response_message = {
                'success': True,
                'message': message
            }
        else:
            response_message = {
                'success': False,
                'message': 'Error '
            }
        return response_message