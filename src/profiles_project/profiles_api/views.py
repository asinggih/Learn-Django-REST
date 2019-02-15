from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions

# ModelViewSet is a special viewset offered by django
# rest framework that takes care of CRUD operations of
# our model items


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations of profiles"""

    # These variable names below are listed in the docs

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # single item tuple. To make sure that it's immutable
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and pass and returns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the obtain auth token  APIView to validate and create a token"""

        # passing request to ObtainAuthToken APIView
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles CRUD operations for profile feed item"""

    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    # isAuthenticatedOrReadOnly is to remove the ability to post status if not logged in
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile feed to the logged in user"""

        serializer.save(user_profile=self.request.user)


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
