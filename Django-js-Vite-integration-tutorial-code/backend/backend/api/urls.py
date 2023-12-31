from rest_framework.routers import DefaultRouter
from post.api.urls import post_router
from django.urls import path, include

router = DefaultRouter()

router.registry.extend(post_router.register('post', PostViewSet))
urlpatterns = [
    path('', include(router.urls)),  
]