from rest_framework import serializers


class ApiNameSerializer(serializers.Serializer):
    """
    Serializes a name field for testing our APIView
    """

    # it will throw an error if API name is longer than 10
    random_quote = serializers.CharField(max_length=10)
