from django.db import models

class Student_info(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    roll_number = models.IntegerField()

