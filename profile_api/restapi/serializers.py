from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
  """serialize a name field four testing to our API """
  name = serializers.CharField(max_length = 13)
