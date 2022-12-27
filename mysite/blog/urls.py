from django.urls import include, path
from rest_framework.routers import DefaultRouter
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('post', views.PostList.as_view(), name='post'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post'),
    path('static_view', views.static_view, name='renderer_classes'),
    path('format_view_blog', views.format_view_blog, name='format_view_blog'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
