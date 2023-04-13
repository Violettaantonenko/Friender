from django.db import models

SEX = [
    ('m', 'male'),
    ('f', 'female'),
]

CATEGORY = [
    (1, 'restaurant'),
    (2, 'cafe'),
    (3, 'bar'),
]
class Users(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField ()
    sex = models.CharField(max_length=1, choices=SEX)
    city = models.CharField(max_length=100, default='Minsk')
    email = models.EmailField(null=True, unique=True)

def __str__(self):
    return str(self.name)

class Establishments(models.Model):
    name = models.CharField(max_length=40)
    category = models.IntegerField(choices=CATEGORY)
    address = models.CharField(max_length=40)
    phone  = models.CharField(max_length=40)

def __str__(self):
    return self.establishments


def __str__(self):
    return self.name


