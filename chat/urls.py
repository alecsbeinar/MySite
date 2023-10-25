import os
from django.urls import path, re_path
from django.views.static import serve
from chat.views import Main, TalkMessages

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app_name = "chat"
urlpatterns = [
    path('', Main.as_view(), name="main"),
    path('messages', TalkMessages.as_view(), name='messages'),

    # Serve up a local static folder to serve spinner.gif
    re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': os.path.join(BASE_DIR, 'static'), 'show_indexes': True},
            name='static'
            )
]
