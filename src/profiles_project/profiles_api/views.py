from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class Hello(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.ApiNameSerializer

    def list(self, request):
        """return a hello message"""

        viewset_list = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps URLs using Routers',
            'provides more functioanlity with less code'
        ]

        return Response({
            'message': "Hello",
            'viewset_list': viewset_list
        })

    def create(self, request):
        """Create a new Hello message"""

        serializer = serializers.ApiNameSerializer(data=request.data)

        if serializer.is_valid():
            # Has to be the same name as what we defined in the serializer
            name = serializer.data.get("random_quote")
            print(name)
            message = "Hello {}".format(name)
            return Response({
                "message": message
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID"""

        return Response({
            "http_method": "GET"
        })

    def update(self, request, pk=None):
        """Handles updating an object"""

        return Response({
            "http_method": "PUT"
        })

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""

        return Response({
            "http_method": "PATCH"
        })

    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({
            "http_method": "DELETE"
        })


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

    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({
            "method": "put"
        })

    def patch(self, request, pk=None):
        """Patch request, only updates fileds provided in the request"""

        return Response({
            'method': 'patch'
        })

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({
            'method': 'delete '
        })
