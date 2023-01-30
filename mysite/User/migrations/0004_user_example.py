from django.db import migrations
from django.contrib.auth.hashers import (
    make_password,
)

def set_password(raw_password):
    return make_password(raw_password)

def create_example_users(apps, schema_editor):
    User = apps.get_model("User", "User")
    obj = User(email='user@mail.it', first_name='name', last_name='surname', password=set_password('password'))
    obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.RunPython(create_example_users)
    ]