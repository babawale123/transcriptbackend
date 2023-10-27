from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,name,password):
        if not email:
            raise ValueError("Please enter an email address")
        if not password:
            raise ValueError('user must provide a valid password')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(PermissionsMixin,AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    def __str__(self):
        return self.email