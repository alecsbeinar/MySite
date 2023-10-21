from django.urls import path
from autos.views import MakeCreate, MakeAll, MakeUpdate, MakeDelete, MainView, AutoCreate, AutoUpdate, AutoDelete

app_name = 'autos'
urlpatterns = [
    path('', MainView.as_view(), name="main"),
    # Make
    path('lookup/', MakeAll.as_view(), name='make_all'),
    path('lookup/create/', MakeCreate.as_view(), name="make_create"),
    path('lookup/<int:pk>/update/', MakeUpdate.as_view(), name="make_update"),
    path('lookup/<int:pk>/delete/', MakeDelete.as_view(), name="make_delete"),
    # Auto
    path('main/create/', AutoCreate.as_view(), name="auto_create"),
    path('main/<int:pk>/update/', AutoUpdate.as_view(), name="auto_update"),
    path('main/<int:pk>/delete/', AutoDelete.as_view(), name="auto_delete"),

]
