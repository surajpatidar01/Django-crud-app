from django.db import models

class Student(models.Model):
    roll_number = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)  # <-- yaha add
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
