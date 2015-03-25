__author__ = 'Alex'
from PyQt4.QtGui import *
import sys
import json
import requests,base64
from PyQt4 import uic
import threading

class Window(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        authThread=threading.Thread(target=self.Auth())
        uiThread=threading.Thread(target=self.UiInit())
        #getRemithread=threading.Thread(target=self.DatosDeRemitentes())
        #getDestiThread=threading.Thread(target=self.DatosDeDestinatarios())
        authThread.start()
        #getRemithread.start()
        #getDestiThread.start()
        uiThread.start()

    def Auth(self):
        username='alex'
        password='admin'
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        self.cabecera = {
                       #"Content-Type" : "application/json",
                       "Authorization": "Basic %s"%(base64string),
                        #"Accept":"application/json"
        }

    """def DatosDeRemitentes(self):
        url="http://192.168.0.2:8000/remitentes"
        response=requests.get(url,headers=self.cabecera)
        print response.json()
        list=response.json()
        print "\nREMITENTES\n"
        for item in list:
            id=item['id']
            nombre=item['nombre']
            correo= item['correo']
            cadena= "\nId: "+str(id)+"\n"+"Nombre: "+nombre+"\n"+"Correo: "+correo
            print cadena"""

    """def DatosDeDestinatarios(self):
        url="http://192.168.0.2:8000/destinatarios"
        response=requests.get(url,headers=self.cabecera)
        print response.json()
        list=response.json()
        print "\nDESTINATARIOS\n"
        for item in list:
            id=item['id']
            nombre=item['nombre']
            correo= item['correo']
            cadena= "\nId: "+str(id)+"\n"+"Nombre: "+nombre+"\n"+"Correo: "+correo
            print cadena"""


    def UiInit(self):
        uic.loadUi("view.ui",self)
        #sendThread=threading.Thread(target=self.SendMail())
        self.btnSend.clicked.connect(self.SendData)

    def SendData(self):
        _from=self.leFrom.text()
        _to=self.leTo.text()
        _subject=self.leSubject.text()
        _message=self.teMessage.toPlainText()

        correo=json.dumps({"remitente":unicode(_from),"destinatario":unicode(_to),"asunto":unicode(_subject),"mensaje":unicode(_message)})

        url = 'http://192.168.0.2:8000/sendMail/'
        username='alex'
        password='admin'
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

        cabeceras = {
                       "Content-Type" : "application/json",
                       "Authorization": "Basic %s"%(base64string),
                        "Accept":"application/json"
        }

        response=requests.post(url,data=correo,headers=cabeceras)
        print response


if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Window()
    ventana.show()
    sys.exit(app.exec_())