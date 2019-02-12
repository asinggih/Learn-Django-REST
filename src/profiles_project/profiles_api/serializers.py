from rest_framework import serializers
from . import models


class ApiNameSerializer(serializers.Serializer):
    """
    Serializes a name field for testing our APIView
    """

    # it will throw an error if API name is longer than 10
    random_quote = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for our User Profile Object"""

    # use the model serializer features, rather than
    # manually defining the fields one by one
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # specifying which field we want to add special args into
        extra_kwargs = {'password': {
            'write_only': True
        }}

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
