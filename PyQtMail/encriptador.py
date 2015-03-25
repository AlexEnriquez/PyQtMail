__author__ = 'Alex'
import base64
username="alex"
mail="djalex12@hotmail.com"
passwd="megaman12"
print base64.encodestring('%s:%s:%s'%(username,passwd,mail)).replace('\n','')
