# Generated by Django 4.2.10 on 2024-02-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('EmailID', models.CharField(max_length=30)),
                ('Subject', models.CharField(max_length=30)),
                ('Message', models.TextField()),
            ],
        ),
    ]
