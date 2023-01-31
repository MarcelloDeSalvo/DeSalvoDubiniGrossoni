# Generated by Django 4.1.5 on 2023-01-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Socket', '0003_rename_socketstatus_socket_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socket',
            name='status',
            field=models.CharField(choices=[('Y', 'Available'), ('N', 'Unavailable'), ('C', 'Charging')], default='Y', max_length=1),
        ),
    ]
