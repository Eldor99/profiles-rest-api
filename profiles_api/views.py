from rest_restframework.views import APIView
from rest_restframework.response import Response

class HelloApiView(APIView):
	""" Test API View """

	def get(self, request, format=None):
		""" Returns a list of APIView features """
		an_apiview = [
			'Uses HTTP methods as function (get, post, path, delete)',
			'Is similar to a traditional Django View',
			'Gives you most control over you application logic',
			'Is mapped manualy to URLs'
		]

		return Response({'message': "Hello", 'an_apiview': an_apiview})