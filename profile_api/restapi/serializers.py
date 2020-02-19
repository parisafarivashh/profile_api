from rest_framework import serializers
from restapi import models

class HelloSerializer(serializers.Serializer):
  """serialize a name field four testing to our API """
  name = serializers.CharField(max_length = 13)

class UserProfileSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Profile
    fields =('name','last_name','phone')
    extra_kwargs={
      'phone':{
        'write_only':True,
        'style':{'input_type':'phone'}
      }
    }

  def create(self,validated_data):
    user = models.Profile(
      name = validated_data['name'],
      last_name = validated_data['last_name'],
      phone = validated_data['phone']
    )  
    return user
