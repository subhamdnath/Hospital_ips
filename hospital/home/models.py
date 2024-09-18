from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from home.constrains import *


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extrafields):

        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email = email, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extrafields):
        extrafields.setdefault("is_staff", True)
        extrafields.setdefault("is_superuser", True)

        if extrafields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff True")
        if extrafields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser True")
        user = self.create_user(email, password, **extrafields)
        return user

        

class User(AbstractUser):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    role_id = models.PositiveIntegerField(choices=ROLE_CHOICES, default=ADMIN, null=True, blank=True)
    password = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return f"{self.email}- {self.role_id}"

    class Meta:
        managed = True
        db_table = "tbl_user"





    
    
