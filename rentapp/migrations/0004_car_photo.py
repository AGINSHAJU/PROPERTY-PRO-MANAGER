# Generated by Django 4.2.10 on 2024-02-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0003_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Photo',
            field=models.ImageField(default='default', upload_to='static/images'),
        ),
    ]
