from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#from PyDrill.views import RemitenteViewSet,DestinatarioViewSet,MailViewSet
from PyDrill.views import MailViewSet
from PyDrill import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
#router.register(r'remitentes',RemitenteViewSet)
#router.register(r'destinatarios',DestinatarioViewSet)
router.register(r'mails',MailViewSet)

urlpatterns = patterns('',
    url(r'^',include(router.urls)),
    url(r'^sendMail/',"PyDrill.views.sendMail",name='sendMail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
