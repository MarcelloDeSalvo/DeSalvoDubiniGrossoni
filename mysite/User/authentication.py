from User.models import User
from rest_framework.authentication import BaseAuthentication

class EmailAuthBackend(BaseAuthentication):
    """
    Custom authentication backend.

    Allows users to log in using their email address.
    """

    def authenticate(self, request, username=None, password=None):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        try:
            user = User.objects.get_by_email(email=username)
            checkPassword = user.check_password(password)
            if checkPassword:
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return User.get_id(pk=user_id)
        except User.DoesNotExist:
            return None