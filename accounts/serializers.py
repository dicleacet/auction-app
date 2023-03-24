from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from accounts.models import User


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {'no_active_account': _('Bu bilgilere ait üyelik bulunamadı, bilgileri kontrol ediniz.')}

    def create(self, validated_data):
        return UserTokenObtainPairSerializer(**validated_data)

    def update(self, instance, validated_data):
        return UserTokenObtainPairSerializer(**validated_data)


class UserTokenRefreshSerializer(TokenRefreshSerializer):

    def create(self, validated_data):
        return UserTokenRefreshSerializer(**validated_data)

    def update(self, instance, validated_data):
        return UserTokenRefreshSerializer(**validated_data)


class UserTokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.ReadOnlyField()

    def create(self, validated_data):
        return UserTokenRefreshResponseSerializer(**validated_data)

    def update(self, instance, validated_data):
        return UserTokenRefreshResponseSerializer(**validated_data)


class PasswordSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        min_length=5,
        max_length=128,
        style={'input_type': 'password'},
        write_only=True,
        required=True,
        allow_null=False
    )
    password2 = serializers.CharField(
        min_length=5,
        max_length=128,
        style={'input_type': 'password'},
        write_only=True,
        required=True,
        allow_null=False
    )

    class Meta:
        model = User
        fields = (
            'password1', 'password2'
        )

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password1': _('Parolalar eşleşmiyor.')}
            )
        return attrs

    def save(self, **kwargs):
        password = self.validated_data.get('password1', False)
        self.instance.set_password(password)
        self.instance.save()
        return self.instance


class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'user_permission', 'last_login',
            'date_joined'
        )
        read_only_fields = fields


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'user_permission', 'date_joined'
        )
        read_only_fields = (
            'id', 'date_joined'
        )

    def validate_user_permission(self, value):
        if value not in ['member', 'manager']:
            raise serializers.ValidationError(
               [_('Geçerli yetki seçiniz.')]
            )
        return value


class CreateUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        min_length=5,
        max_length=128,
        style={'input_type': 'password'},
        write_only=True,
        required=True,
        allow_null=False
    )
    password2 = serializers.CharField(
        min_length=5,
        max_length=128,
        style={'input_type': 'password'},
        write_only=True,
        required=True,
        allow_null=False
    )

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'user_permission', 'is_active',
            'password1', 'password2', 'date_joined'
        )
        read_only_fields = (
            'id', 'is_active', 'date_joined'
        )

    def validate_user_permission(self, value):
        if value not in ['member', 'manager']:
            raise serializers.ValidationError(
               [_('Geçerli yetki seçiniz.')]
            )
        return value

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                [_('Parolalar eşleşmiyor.')]
            )
        return attrs

    def create(self, validated_data):
        validated_data['password'] = validated_data.pop('password1')
        validated_data.pop('password2')
        self.instance = User.objects.custom_create_user(**validated_data)
        return self.instance


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email', 'user_permission'
        )
        read_only_fields = fields


class SubUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email'
        )
        read_only_fields = fields


class UserPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_null=False, allow_blank=False)

    def create(self, validated_data):
        return UserPasswordResetEmailSerializer(**validated_data)

    def update(self, instance, validated_data):
        return UserPasswordResetEmailSerializer(**validated_data)


class UserPasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    password1 = serializers.CharField(
        min_length=5, max_length=128, style={'input_type': 'password'}, write_only=True,
        required=True, allow_null=False
    )
    password2 = serializers.CharField(
        min_length=5, max_length=128, style={'input_type': 'password'}, write_only=True,
        required=True, allow_null=False
    )

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password1': _('Parolalar eşleşmiyor.')}
            )
        return attrs

    def create(self, validated_data):
        return UserPasswordResetSerializer(**validated_data)

    def update(self, instance, validated_data):
        return UserPasswordResetSerializer(**validated_data)
