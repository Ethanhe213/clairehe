from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery,name='gallery'),
    path('photo/<str:pk>', views.viewphoto,name='photo'),
    path('add/', views.addPhoto,name='add'),
    path('add-video/', views.addVideo,name='add-video'),
    path('delete/photo/<str:pk>', views.deletephoto,name='delete'),
    path('delete/video/<str:pk>', views.deletevideo,name='delete-video'),
    path('video/<str:pk>', views.viewvideo,name='video'),
    path('video/', views.gallery_video,name='video-gallery'),
]