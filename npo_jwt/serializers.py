from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from npo_user.models import NPOUser


class NPOObtainPairSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(NPOObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


class UserFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPOUser
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email')


class UserDuplicateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPOUser
        fields = ('username', 'first_name', 'last_name')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=NPOUser.objects.all())]
    )

    password = serializers.CharField(write_only=True,
                                     required=True, validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = NPOUser
        fields = ('username', 'password', 'password2', 'email')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': 'Password fields did not match'})
        return attrs

    def validate_username(self, value):
        data = self.get_initial()
        username = data.get('username')
        username_qs = NPOUser.objects.filter(username=username)
        if username_qs.exists():
            duplicate_obj = NPOUser.objects.get(username=username)
            serializer = UserDuplicateSerializer(duplicate_obj)
            raise ValidationError('This username has been registered!' + str(serializer.data))
        else:
            pass
        return value

    def create(self, validated_data):
        user = NPOUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
