from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from users.permissions import IsOwnerOrSuperuser
from users.serializers import UserSerializer, LoginSerializer, RegisterSerializer, ChangePasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'delete', 'options', 'put', 'patch']
    permission_classes = [IsOwnerOrSuperuser]

    def list(self, request, *args, **kwargs):
        raise NotImplemented()

    def create(self, request, *args, **kwargs):
        raise NotImplemented()

class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

class LogInView(TokenObtainPairView):
    serializer_class = LoginSerializer

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    http_method_names = ['put']
    def get_object(self):
        return self.request.user
