from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
import os

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/main.html')),
    path('polls/', include('polls.urls')),
    path('autos/', include('autos.urls')),
    path('ads/', include('ads.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]