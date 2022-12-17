from django.urls import include, path
from rest_framework.routers import DefaultRouter
from blog import views


urlpatterns = [
    path('post', views.post, name='post'),
    path('post/<int:pk>', views.post_detail, name='post')
]
