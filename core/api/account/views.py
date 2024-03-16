from rest_framework import generics, permissions
from core import models, utils
from core.api.account.serializers import AccountSerializer, PasswordChangeSerializer
from core.api.auth.token import TokenObtainPairSerializer
from rest_framework import response, status, parsers

class UpdateView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = AccountSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        token = TokenObtainPairSerializer().get_token(self.request.user)
        return response.Response({
            'refresh': str(token),
            'access': str(token.access_token)
        }, status=status.HTTP_200_OK)

class DeleteView(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = AccountSerializer

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())
        return response.Response({
            'message': 'User deleted successfully.'
        }, status=status.HTTP_204_NO_CONTENT)

class PasswordChangeView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = PasswordChangeSerializer

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({
            'message': 'Password updated successfully.'
        }, status=status.HTTP_200_OK)