# Generated by Django 3.2.8 on 2021-10-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='no-image.png', upload_to='avatars'),
        ),
    ]
