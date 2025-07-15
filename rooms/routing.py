# from django.urls import path

# from . import consumers

# websocket_urlpatterns= [
#     path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
# ]

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
