from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from restapi import serializers

class HelloApiVeiw(APIView):
  """test api view"""
  serializer_class = serializers.HelloSerializer
  def get(self,request,format=None):
    """Rutern a list of APIVIEW features """
    an_apiview=[
      'uses http method as function (get,post,patch,put,delete)',
      'is similar to a traditional django view', 
      'Gives you the most control over you application logic',
      'is mapped manually to urls',

    ]
    return Response({'message':'hello','an_apiview':an_apiview})

  def post(self,request):
    """Creat hello message with our name """
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')

      message ="HELLO {}".format(name)
      return Response({'message':message})
    
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )

  def put(self,request,pk=None):
    return Response({'method':'PUT'})

  def patch(self,request,pk=None):
    return Response({'method':'PATCH'})

  def delete(self,request,pk=None):
    return Response({'method':'DELETE'})

