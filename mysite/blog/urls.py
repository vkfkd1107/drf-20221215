from django.urls import include, path
from rest_framework.routers import DefaultRouter
from blog import views


urlpatterns = [
    path('post', views.PostList.as_view(), name='post'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post'),
]
