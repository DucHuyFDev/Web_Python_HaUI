from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
    mssv = models.CharField(max_length=15)
    hoten = models.CharField(max_length=200)
    email = models.EmailField()
    khoa = models.CharField(choices=[
        ("cntt", "Công nghệ thông tin"),
        ("ck", "Cơ khí"),
        ("dt", "Điện tử"),
    ])
    maths = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    physics = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    chemistry = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    
