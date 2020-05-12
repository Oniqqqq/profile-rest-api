from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

from .views import HelloViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
