from django.http import HttpResponse
from .text_message import TextMessage

def send(request):
  sms = TextMessage("0727686700","Mesaj de test")
  sms.connectPhone()
  sms.sendMessage()
  sms.disconnectPhone()

  return HttpResponse('{"test": true}', content_type='application/json');