from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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


class HelloViewSet(viewsets.ViewSet):

  """Test Api Viewset"""
  serializer_class = serializers.HelloSerializer


  def list(self,request):
    """return hello message """
    a_viewset =[
      'uses action (list,creat,retrieve,update,partial_update)',
      'automaticlly maps to urls using routers',
      'provide more functionality with less code ',

    ]
    return Response({'message':'hello','a_viewset':a_viewset})

  def create(self,request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message ="hello {}".format(name) 
      return Response({'message':message})

    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST

      ) 

  def retrieve(self,request,pk=None):
    return Response({'http_method':'GET'}) 

  def update(self,request,pk=None):
    return Response({'http_method':'PUT'})

  def partial_update(self,request,pk=None):
    return Response({'http_method':'PATCH'})

  def destroy(self,request,pk=None):
    return Response({'http_method':'DELETE'})     


