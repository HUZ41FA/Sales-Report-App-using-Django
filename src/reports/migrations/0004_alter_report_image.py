# Generated by Django 3.2.8 on 2021-11-17 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_report_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='new directory'),
        ),
    ]
