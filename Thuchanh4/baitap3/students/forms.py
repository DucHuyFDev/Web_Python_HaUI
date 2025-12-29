from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta():
        model = models.Student
        fields = "__all__"
        labels = {
            "mssv": "Mã sinh viên",
            "hoten": "Họ tên",
            "email": "Email",
            "khoa": "Khoa",
            "maths": "Điểm toán",
            "physics": "Điểm lý",
            "chemistry": "Điểm hóa",
       }