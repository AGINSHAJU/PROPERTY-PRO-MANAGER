# Generated by Django 4.2.10 on 2024-02-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0007_booking_carname'),
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place', models.CharField(max_length=20)),
                ('Type', models.CharField(max_length=20)),
                ('Rate', models.IntegerField()),
                ('Description', models.TextField()),
                ('Photo', models.ImageField(upload_to='static/images')),
            ],
        ),
    ]
