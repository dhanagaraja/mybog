# Generated by Django 4.1.1 on 2022-12-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_Picture',
            field=models.ImageField(default='media/profile/default.png', upload_to='media/profile/'),
        ),
    ]
