# Generated by Django 4.1.1 on 2022-11-13 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_profile_user_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_Picture',
            field=models.ImageField(upload_to='static/profile/'),
        ),
    ]
