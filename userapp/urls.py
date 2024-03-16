from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profil/<int:pk>/', UserRetrieveUpdateDestroyView.as_view())
]
