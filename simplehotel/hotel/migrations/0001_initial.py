# Generated by Django 5.0 on 2024-01-05 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_date', models.DateTimeField()),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('headcount', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('room_type', models.CharField(choices=[('twn', 'ツイン'), ('dbl', 'ダブル'), ('sng', 'シングル')], max_length=50)),
            ],
        ),
    ]
