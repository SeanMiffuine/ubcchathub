from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer) # regex of w+ matches any word and /$ matches end of word, so no extended URl
]