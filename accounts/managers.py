from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError(_('Kullanıcı adı alanı zorunludur.'))

        user = self.model(
            username=username,
            email=self.normalize_email(email) if email else None
        )
        user.set_password(password)
        user.user_permission = 'member'
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username,
            email=email if email else None,
            password=password,
        )
        user.user_permission = 'superuser'
        user.save(using=self._db)
        return user

    def custom_create_user(self, username, email=None, password=None, **kwargs):
        """
        Creates and saves a User with the given serializer data.
        """
        if not username:
            raise ValueError(_('Kullanıcı adı alanı zorunludur.'))

        user = self.model(
            username=username,
            email=self.normalize_email(email) if email else None,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
