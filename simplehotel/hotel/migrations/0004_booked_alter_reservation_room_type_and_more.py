# Generated by Django 5.0 on 2024-01-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('twn_booked', models.IntegerField(default=0)),
                ('dbl_booked', models.IntegerField(default=0)),
                ('sgl_booked', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_type',
            field=models.CharField(choices=[('twn', 'ツイン'), ('dbl', 'ダブル'), ('sgl', 'シングル')], max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('twn', 'ツイン'), ('dbl', 'ダブル'), ('sgl', 'シングル')], max_length=50),
        ),
    ]
