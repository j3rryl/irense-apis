
class ResponseMessages():
    def create_entity(self, success):
        if success:
            response_message = {
                'success': True,
                'message': self + ' created successfully'
            }
        else:
            response_message = {
                'success': False,
                'message': 'Error creating '+ self
            }
        return response_message