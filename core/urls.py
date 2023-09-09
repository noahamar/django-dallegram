from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('/post/post_id:string', views.index, name='index'),
]