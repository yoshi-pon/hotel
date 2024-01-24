from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    ROOM_TYPES = (
        ('twn', 'ツイン'),
        ('dbl', 'ダブル'),
        ('sgl', 'シングル'),
        )
    
    created_at = models.DateTimeField(default=timezone.now)
    checkin = models.DateField()
    checkout = models.DateField()
    headcount = models.IntegerField()
    name = models.CharField(max_length=40)
    email = models.EmailField()
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_NUMBER = (
        ('201', '201'),
        ('202', '202'),
        ('203', '203'),
        ('204', '204'),
        ('205', '205'),
        ('301', '301'),
        ('302', '302'),
        ('303', '303'),
        ('304', '304'),
        ('305', '305'),
        ('401', '401'),
        ('402', '402'),
        ('403', '403'),
        ('404', '404'),
        ('405', '405'),
        ('501', '501'),
        ('502', '502'),
        ('503', '503'),
        ('504', '504'),
        ('505', '505'),
        )

    ROOM_TYPES = (
        ('twn', 'ツイン'),
        ('dbl', 'ダブル'),
        ('sgl', 'シングル'),
        )

    MAX_HEADCOUT = (
        (1, 1),
        (2, 2),
        )
        
    room_number = models.CharField(max_length=40, \
                                   choices=ROOM_NUMBER, unique=True)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    max_headcount = models.IntegerField(choices=MAX_HEADCOUT)

    def __str__(self):
        return self.room_number


class Booked(models.Model):
    date = models.DateField(unique=True)
    twin_booked = models.IntegerField(default=0)
    double_booked = models.IntegerField(default=0)
    single_booked = models.IntegerField(default=0)

    def __str__(self):
        return self.date.strftime('%Y/%m/%d')
