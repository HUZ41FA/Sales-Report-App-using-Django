# Generated by Django 3.2.8 on 2021-10-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(null=True, upload_to='charts'),
        ),
    ]
