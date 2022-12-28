from django.urls import include, path
from rest_framework.routers import DefaultRouter
from todo import views
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()
router.register('todo', views.TodoViewSet)


urlpatterns = [
    path('', include(router.urls))
]
