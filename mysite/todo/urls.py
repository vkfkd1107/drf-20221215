from django.urls import include, path
from rest_framework.routers import DefaultRouter
from todo import views

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('todo-list', views.TodoList.as_view(), name='todo_list'),
    path('todo/<int:pk>/', views.TodoDetail.as_view(), name='todo_detail'),
]
