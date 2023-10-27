from django.urls import path
from .views import SignupView,SignInView

urlpatterns = [
    path('',SignupView.as_view()),
    path('login/', SignInView.as_view())
]