from judge_reg.models import RegistroJuridico
from rest_framework import serializers


class RegistroJuridicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistroJuridico
        fields = ['n_processo',
                  'id_cliente',
                  'favor_contribuinte',
                  'ementa']
