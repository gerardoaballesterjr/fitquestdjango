from rest_framework import generics, permissions
from core import models
from core.api.auth.serializers import UserSerializer
from core.api.auth.token import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import response, status

class RegisterView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    permission_classes = [permissions.AllowAny,]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token = TokenObtainPairSerializer().get_token(serializer.instance)
        return response.Response({
            'refresh': str(token),
            'access': str(token.access_token)
        }, status=status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer