from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

# Create your models here.
ADMIN = 1
CLIENT = 2
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (CLIENT, 'CLIENT'),
)


class NPOUser(AbstractBaseUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE,
                                    verbose_name='Тип Пользователя',
                                    default=CLIENT)
    username = models.CharField('username',
                                unique=True,
                                max_length=100)
    email = models.EmailField('email', null=True,
                              max_length=100, unique=True)
    first_name = models.CharField('first name', max_length=30,
                                  blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    data_joined = models.DateTimeField('data joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

