from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiVeiw(APIView):
  """test api view"""
  def get(self,request,format=None):
    """Rutern a list of APIVIEW features """
    an_apiview=[
      'uses http method as function (get,post,patch,put,delete)',
      'is similar to a traditional django view', 
      'Gives you the most control over you application logic',
      'is mapped manually to urls',

    ]
    return Response({'message':'hello','an_apiview':an_apiview})

