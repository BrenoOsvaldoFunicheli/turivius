from django.urls import path, include
from django.conf.urls import url


from users.api.viewsets import create_user

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    
    path('create_user/',create_user),
]
