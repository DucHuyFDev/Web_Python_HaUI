from django import forms

class StudentForm(forms.Form):
    mssv = forms.CharField(label="Mã sinh viên", max_length=15, widget = forms.TextInput({
        "placeholder": "Nhập mã sinh viên"
    }))
    hoten = forms.CharField(label="Họ và tên", max_length=100, widget = forms.TextInput({
        "placeholder": "Nhập tên"
    }))
    email = forms.EmailField(label="Email", widget = forms.TextInput({
        "placeholder": "Nhập email"
    }))
    khoa = forms.ChoiceField(choices=[
        ("cntt", "Công nghệ thông tin"),
        ("ck", "Cơ khí"),
        ("dt", "Điện tử"),
    ], widget=forms.Select())