from django.db import models
class Student(models.Model):
    roll_number = models.IntegerField()
    F_name = models.CharField(max_length=30)
    L_name = models.CharField(max_length = 30)
    Address = models.CharField(max_length =50)
    MO_no = models.IntegerField()

    def __str__(self):
        return self.F_name





# Create your models here.
