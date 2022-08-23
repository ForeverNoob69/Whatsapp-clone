from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getData),
    path('room-data',views.getRoomData),
    path('user-data',views.getUserData),
    path('profile-data/<str:pk>',views.getProfileData),
    path('profile-data',views.createProfileData),
    path('update-data/<str:pk>',views.updateRoomData),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
