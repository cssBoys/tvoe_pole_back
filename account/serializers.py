from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'phone', 'password', 'email', 'name', 'surname', 'balance')
        write_only_fields = ('password', )
        read_only_fields = ('id', )

    def create(self, validate_data):
        password = validate_data.pop('password')
        user = CustomUser.objects.create(
            **validate_data
        )
        user.set_password(password)
        user.save()
        return user