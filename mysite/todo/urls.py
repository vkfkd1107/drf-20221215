from django.urls import include, path
from rest_framework.routers import DefaultRouter
from todo import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('post/', views.TodoList.as_view(), name='post'),
    path('post/<int:pk>', views.TodoDetail.as_view(), name='post'),
    path('static_html_renderer', views.static_html_renderer, name='static_html_renderer'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
