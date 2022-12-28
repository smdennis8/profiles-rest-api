from unittest.util import _MAX_LENGTH
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    '''Serializes a name field for teting our APIView'''
    '''Take care of validation rules'''
    name = serializers.CharField(max_length=10)
