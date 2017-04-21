from django.http import HttpResponse
from .text_message import TextMessage
from django.views.decorators.http import require_http_methods
from .payload import Payload

@require_http_methods(["POST"])
def send(request):
  p = Payload(request.body)
  sms = TextMessage(p.recipient, p.message)
  sms.run()

  return HttpResponse(request.body, content_type='application/json');