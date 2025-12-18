from django.urls import path
from .views import RegisterView, UserRecoveryUpdateView, PasswordResetView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path('recovery/', UserRecoveryUpdateView.as_view(), name='user-recovery'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
]
