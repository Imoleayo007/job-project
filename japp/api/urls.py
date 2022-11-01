from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
     path('register/', views.user_registration, name='register'),
     path('token/', obtain_auth_token, name='token'),
     path("login", views.login_view), 
     path("logout", views.login_view), 
     # path('auth/refresh/', TokenRefreshView().as_view(), name="refresh_token"),
]