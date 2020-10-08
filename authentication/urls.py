from django.urls import path
from .views import RegisterView,VerifyEmail,LoginAPIView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('email-verify/',VerifyEmail.as_view(),name='email-verify'),
    path('login/',LoginAPIView.as_view(),name='login'),
]
