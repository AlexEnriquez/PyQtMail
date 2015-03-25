from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import viewsets
#from models import Remitente,Destinatario,Mail
from models import Mail
#from serializer import RemitenteSerializer,DestinatarioSerializer,MailSerializer
from serializer import MailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from rest_framework.views import APIView
#class RemitenteViewSet(viewsets.ModelViewSet):
    #serializer_class = RemitenteSerializer
    #queryset = Remitente.objects.all()

#class DestinatarioViewSet(viewsets.ModelViewSet):
    #serializer_class = DestinatarioSerializer
    #queryset = Destinatario.objects.all()

class MailViewSet(viewsets.ModelViewSet):
    serializer_class = MailSerializer
    queryset=Mail.objects.all()

@api_view (['GET','POST'])
def sendMail(request):
    if request.method=='GET':
        mail=Mail.objects.all()
        serializer=MailSerializer(mail,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=MailSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            remitente=request.DATA['remitente']
            destinatario=request.DATA['destinatario']
            asunto=request.DATA['asunto']
            mensaje=request.DATA['mensaje']

            msg = EmailMultiAlternatives(
            subject="%s"%asunto,
            body="This is the text email body",
            from_email="<%s>"%remitente,
            to=["Recipient One <%s>"%destinatario],
            headers={'Reply-To': "Service <support@example.com>"} # optional extra headers
            )
            msg.attach_alternative("<p>%s</p>"%mensaje, "text/html")
            msg.tags = ["one tag", "two tag", "red tag", "blue tag"]
            msg.metadata = {'user_id': "8675309"}
            msg.send()
            return Response("Mail sent to: %s"%destinatario)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
