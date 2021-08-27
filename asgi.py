import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from turbo.consumers import TurboStreamsConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'turbodjango.settings')


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": TurboStreamsConsumer.as_asgi()  # Leave off .as_asgi() if using Channels 2.x
})