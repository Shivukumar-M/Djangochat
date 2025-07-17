
# import os
# import django
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack 
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djchatapp.settings')


# django.setup()


# import rooms.routing


# def get_default_application():
#     from django.core.asgi import get_asgi_application
#     return get_asgi_application()

# application = ProtocolTypeRouter({
#     "http": get_default_application(), 
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             rooms.routing.websocket_urlpatterns 
#         )
#     ),
# })




import os
import django 


from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djchatapp.settings') 
django.setup()
import rooms.routing

# django_asgi_app = django.core.asgi.get_asgi_application()
def get_default_application():
    from django.core.asgi import get_asgi_application
    return get_asgi_application()


application = ProtocolTypeRouter({
   
    "http": get_default_application(),

    
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(  
            URLRouter(
                rooms.routing.websocket_urlpatterns 
            )
        )
    ),
})
