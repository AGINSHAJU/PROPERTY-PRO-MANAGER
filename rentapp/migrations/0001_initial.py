# Generated by Django 4.2.10 on 2024-02-19 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('EmailID', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
                ('CPassword', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=30)),
            ],
        ),
    ]
