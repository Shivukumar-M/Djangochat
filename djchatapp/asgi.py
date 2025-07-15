
import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djchatapp.settings')


django.setup()


import rooms.routing


def get_default_application():
    from django.core.asgi import get_asgi_application
    return get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_default_application(), 
    "websocket": AuthMiddlewareStack(
        URLRouter(
            rooms.routing.websocket_urlpatterns 
        )
    ),
})