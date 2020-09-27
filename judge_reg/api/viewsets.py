#   import models of the auth django's package
from django.contrib.auth.models import User, Group
from django.db.models import Sum, Count
from django.core import serializers


#   rest frameworks's response
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

# my classes
from judge_reg.models import RegistroJuridico
from judge_reg.api.serializers import RegistroJuridicoSerializer
import json

unavailable_resource = Response({"result": "this resource isn't available"}, status=status.HTTP_404_NOT_FOUND)


class RegistroJuridicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Judge Registre to be viewed
    """
    queryset = RegistroJuridico.objects.all()
    serializer_class = RegistroJuridicoSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def contagem(self, request):
        response_data = RegistroJuridico.objects.filter(id_cliente=3).values('id_cliente','favor_contribuinte').annotate(Count('favor_contribuinte'))
     
        return Response({"results":list(response_data)})
     