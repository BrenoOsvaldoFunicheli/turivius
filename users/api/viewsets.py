#   import models of the auth django's package
from django.contrib.auth.models import User, Group

#   rest frameworks's response
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, action


unavailable_resource = Response({"result": "this resource isn't available"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@action(detail=True, methods=['get', 'post'])
def create_user(request):
    """
    This Endpoint is valid  to create user authentication
    --- 
    
    post:
        -username: A username
        -email: A E-mail valid
        -password: A password of user
    """
    
    if request.method == 'POST':
        data = request.data

        user, created = User.objects.get_or_create(username=data['username'], email=data['email'])

        if created:
            user.set_password(data['password'])
            user.save()
            
        return Response({"User Created":"User Created"})
    else:
        return unavailable_resource
        
