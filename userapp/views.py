from rest_framework.generics import *
from rest_framework.permissions import *

from .serializers import *


class UserRegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = UserAdmin.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = UserAdmin.objects.all()

