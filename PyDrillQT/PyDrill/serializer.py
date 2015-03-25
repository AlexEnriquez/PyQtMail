__author__ = 'Alex'
from rest_framework import serializers
#from PyDrill.models import Remitente, Destinatario, Mail
from PyDrill.models import Mail

"""class RemitenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remitente
        fields = ('id','nombre','correo',)

class DestinatarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinatario
        fields = ('id','nombre','correo')"""

class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ('id','remitente','destinatario','asunto','mensaje',)