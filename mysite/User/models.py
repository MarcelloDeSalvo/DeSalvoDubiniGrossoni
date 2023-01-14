from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

class AccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None, is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not first_name or not last_name:
            raise ValueError('Users must have a name and a surname')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)  # a superuser
    staff = models.BooleanField(default=False)
    services = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return ('[email: ' + self.email + ', first name: ' + self.first_name + ', last name: ' + self.last_name + ']')

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def complete_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin