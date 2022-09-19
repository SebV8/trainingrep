from datetime import date
from time import time
from django.db import models

# Create your models here.
class Pr_detail(models.Model):
    BackSquat = 'BS'
    FrontSquat = 'FS'
    DeadLift = 'DL'
    Clean = 'CL'
    Snatch = 'SN'
    categorias = [
        (BackSquat, 'Back Squat'),
        (FrontSquat, 'Front Squat'),
        (DeadLift, 'Dead Lift'),
        (Clean, 'Clean'),
        (Snatch, 'Snatch'),
    ]
    class Meta:
        ordering = ('name', '-date')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, choices=categorias, default=BackSquat)
    weight = models.CharField(max_length=100)
    reps = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Rm_detail(models.Model):
    ToesToBar = 'TTB'
    PullUp = 'PU'
    ChestToBar = 'CTB'
    WallBall = 'WB'
    SimpleUnder = 'SU'
    DoubleUnder = 'DU'
    Burpee = 'BR'
    categorias_rm = [
        (ToesToBar, 'Toes To Bar'),
        (PullUp, 'Pull Up'),
        (ChestToBar, 'Chest To Bar'),
        (WallBall, 'Wall Ball'),
        (SimpleUnder, 'Simple Under'),
        (DoubleUnder, 'Double Under'),
        (Burpee, 'Burpee'),
    ]
    class Meta:
        ordering = ('name', '-date')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, choices=categorias_rm, default=ToesToBar, null=True)
    weight = models.CharField(max_length=100)
    reps = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

class TimeCap_detail(models.Model):
    Nombre = 'NM'
    categorias = [
        (Nombre, 'Nombre'),
    ]
    class Meta:
        ordering = ('name', '-date')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, choices=categorias, default=Nombre)
    time = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name
   