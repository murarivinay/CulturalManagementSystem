# Generated by Django 5.0.1 on 2024-04-23 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='name',
            new_name='username',
        ),
    ]
