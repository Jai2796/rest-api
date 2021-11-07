from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API biew features"""

        an_apiview = [
        'Uses HTTp methods as fuhnction (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your logicview',
        'Is mapped manuallyh to URLs',
        ]

        return Response({'message' : 'Hello', 'an apiview' : an_apiview})
