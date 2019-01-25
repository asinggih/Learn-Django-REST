from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class ApiNameHere(APIView):
    """
    Test API View.
    This is inside the doctest of the class
    """

    # It tells Django that the serializer class of this API view
    # is gonna be the ApiNameSerializer class from serializers
    serializer_class = serializers.ApiNameSerializer

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

    def post(self, request):
        """Returns a message with the inserted quote"""

        # serialise the payload of the POST request
        serializer = serializers.ApiNameSerializer(data=request.data)

        if serializer.is_valid():
            # the data that we get has to be the something that we defined
            # inside the serializser of this particular API class
            quote = serializer.data.get('random_quote')
            message = "you say {}".format(quote)
            return Response({
                "message": message
            })

        # standardised error response if serializser is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
