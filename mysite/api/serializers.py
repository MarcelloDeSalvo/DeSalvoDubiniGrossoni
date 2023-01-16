from User.models import User, AccountManager
from django.contrib.auth.password_validation import validate_password
from User.authentication import EmailAuthBackend
from django.core.validators import validate_email
from rest_framework import serializers

#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "first_name", "last_name", "email"]

# Login Serializer
class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * email.
      * password.
    It will try to authenticate the user with when validated.
    """
    email = serializers.EmailField(
        label="email",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'email', 'placeholder': 'Email'}
    )

    password = serializers.CharField(
        label="password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get('email')
        password = attrs.get('password')
        
        emailAuth = EmailAuthBackend()

        if email and password:
            # Try to authenticate the user using Django auth framework.
            user = emailAuth.authenticate(request=self.context.get('request'), username=email, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):

  email = serializers.EmailField(
    required=True,
    validators=[validate_email]
  )

  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

  password2 = serializers.CharField(write_only=True, required=True)

  class Meta:
    model = User
    fields = ('password', 'password2', 'email', 'first_name', 'last_name')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True}
    }

  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs

  def create(self, validated_data):
    user = AccountManager.create_user(
        self,
        validated_data['email'],
        validated_data['first_name'],
        validated_data['last_name'],
        validated_data['password'],
    )
    return user


