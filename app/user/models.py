from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import(
 BaseUserManager,
 AbstractBaseUser,
 PermissionsMixin
)

# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the
    unique indeitifer for auth instead of username
    """
    
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with email and pass
        """
        if not email:
            raise ValueError(_("The email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser with email and pass
        """
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Super user must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Super user must have is_superuser=True"))
        return self.create_user(email,password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
