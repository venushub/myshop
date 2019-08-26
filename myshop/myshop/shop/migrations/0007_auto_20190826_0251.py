# Generated by Django 2.2.4 on 2019-08-26 02:51

from django.db import migrations
from django.contrib.auth.models import User


def create_users(apps, schema_editor):
    user1 = User.objects.create_user('testuser1', 'testuser1@myshop.com', 'shop@123')
    user1.save()

    user2 = User.objects.create_user('testuser2', 'testuser2@myshop.com', 'shop@123')
    user2.save()


class Migration(migrations.Migration):


    dependencies = [
        ('shop', '0006_auto_20190825_2259'),
    ]

    operations = [
        migrations.RunPython(create_users)
    ]