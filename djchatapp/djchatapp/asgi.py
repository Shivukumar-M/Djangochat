import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import rooms.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djchatapp.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            rooms.routing.websocket_urlpatterns
        )
    ),
})
