from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class ApiNameHere(APIView):
    """
    Test API View.
    This is inside the doctest of the class
    """

    # API View lets us define standard HTTP methods

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        apiview_list = [
            'Use standard HTTP methods as functions',
            'similar to a traditional Django view',
            'Gives most control to our logic',
            'mapped to url',
        ]

        return Response({       # will be converted to JSON by Django
            'message': 'Hello',
            'apiview_list': apiview_list
        })
