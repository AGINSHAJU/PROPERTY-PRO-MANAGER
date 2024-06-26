# Generated by Django 4.2.10 on 2024-02-23 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0004_car_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Date', models.DateField()),
                ('Days', models.IntegerField()),
                ('Proof', models.FileField(upload_to='static/proof')),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
