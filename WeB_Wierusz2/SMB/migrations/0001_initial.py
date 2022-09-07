# Generated by Django 4.1 on 2022-09-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMB_new_people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('age', models.CharField(max_length=3, verbose_name='Возраст')),
                ('gender', models.CharField(max_length=8, verbose_name='Пол')),
                ('add_info', models.TextField(blank=True, verbose_name='Противопоказания по физ.нагрузкам (если имеются)')),
                ('phone_number', models.CharField(max_length=25, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Заявки в секцию СМБ',
            },
        ),
    ]