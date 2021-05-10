"""
Account views
"""
from django.core.cache import cache
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from account.models import CustomUser
from account.serializers import UserSerializer
from account.utils import generate_code


class UserCreateView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    User creation view
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )


    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    @action(detail=False, methods=['POST'])
    def code(self, request, *args, **kwargs):
        """
        Access SMS code for auth user
        """
        data = request.data
        value = cache.get(str(data.get('id')))
        if value:
            if value == data.get('code'):
                CustomUser.objects.filter(id=data.get('id')).update(is_active=True)
                return Response({'message': 'ok'}, status=200)
            else:
                return Response({'message': 'Код введен неверно'}, status=406)
        return Response({'message': 'Код уже не действителен'}, status=406)


    @action(detail=False, methods=['POST'])
    def resend(self, request, *args, **kwargs):
        """
        Resend
        """
        try:
            user = CustomUser.objects.get(id = request.data.get('id'))
            generate_code(user.id, user.phone)
            return Response({'message': 'ok'}, status=200)
        except Exception:
            return Response({'message': 'Что то пошло не так'}, status=406)


