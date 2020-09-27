from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, AllowAny
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# rest_framework imports
from rest_framework import routers
from django.views.generic import TemplateView

#   jwt imports
from rest_framework_simplejwt import views as jwt_views


# rest_framework imports
from rest_framework import routers

#   my serializers class

from judge_reg.api.viewsets import  RegistroJuridicoViewSet


# it's defining the routers to api access
router = routers.DefaultRouter()
router.register(r'legal_record', RegistroJuridicoViewSet, 'judge_reg')


urlpatterns = [
    # admin pages
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('users.urls')),

    # autentication
    path('api/v1/authentication/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    

]