from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from account.models import CustomUser
from account.serializers import UserSerializer


class UserCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    @action(detail=False, methods=['POST'])
    def code(self, request, *args, **kwargs):
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
        data = request.data
        cache.set(str(data.get('id')), '7777', 60 * 3)
        return Response({'message': 'ok'}, status=200)