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


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):

  email = serializers.EmailField(
    required=True,
    validators=[validate_email]
  )

  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

  password2 = serializers.CharField(write_only=True, required=True)

  _db = 'default'

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


