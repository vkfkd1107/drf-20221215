from django.urls import include, path
from rest_framework.routers import DefaultRouter
from todo import views

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path(
        'todo',
        views.TodoListAPIView.as_view(),
        name='todo'
    ),
    path(
        'todo/<int:pk>',
        views.TodoDetailAPIView.as_view(),
        name='todo_detail'
    ),
]
