from django.urls import path, reverse_lazy
from ads.views import *

app_name = 'ads'
urlpatterns = [
    path('', AdListView.as_view(), name="all"),
    path('ad/<int:pk>/', AdDetailView.as_view(), name="ad_detail"),
    path('ad/create/', AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name="ad_create"),
    path('ad/<int:pk>/update', AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name="ad_update"),
    path('ad/<int:pk>/delete',
         OwnerDeleteView.as_view(success_url=reverse_lazy(app_name+':all'),
                                 model=Ad,
                                 template_name=f"{app_name}/delete.html"),
         name="ad_delete"),
    path('ad_picture/<int:pk>', stream_file, name='ad_picture'),
    path('ad/<int:pk>/comment', CommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='ad_comment_delete'),
    path('ad/<int:pk>/favorite', AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite', DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]