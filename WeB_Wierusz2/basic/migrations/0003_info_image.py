# Generated by Django 4.1 on 2022-09-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]