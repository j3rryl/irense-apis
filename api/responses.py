
class ResponseMessages():
    def create_entity(self, success):
        if success:
            response_message = {
                'success': True,
                'message': f'{self} created successfully.'
            }
        else:
            response_message = {
                'success': False,
                'message': f'Error creating {self}.'
            }
        return response_message

    def modify_entity(self, success, method):
        message = ''
        if method == 'GET':
            message = f'{self} fetched successfully.'
        elif method == 'PUT':
            message = f'{self} updated successfully.'
        elif method == 'DELETE':
            message = f'{self} deleted successfully.'
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