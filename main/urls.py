from django.urls import path, re_path

from . import views

urlpatterns= [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("upload/", views.upload, name="upload"),
    re_path(
        r'^delete-image/(?P<id>\d+)/(?P<loc>[a-zA-Z]+)/$', 
        views.delete_image, 
        name="delete_image"),
    path('search/', views.search, name='search'),
]