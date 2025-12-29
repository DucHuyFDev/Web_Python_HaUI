from django import forms

class UserForm(forms.Form):
    hoten = forms.CharField(label="Họ và tên", widget=forms.TextInput({
        "placeholder": ""
    }))

    gioitinh = forms.ChoiceField(label="Giới tính", choices=[
        ("m", "Nam"),
        ("f", "Nữ")
    ], widget = forms.Select({
        "class": "form-control"
    }))

    sothich = forms.MultipleChoiceField(label= "Sở thích", choices=[
        ('code', "Lập trình"),
        ('game', "Chơi game"),
        ('sleep', "Ngủ"),
    ], widget= forms.CheckboxSelectMultiple({
        "class": "form-control"
    }))

    ngaysinh = forms.DateField(label = "Ngày sinh", widget=forms.DateInput({
        "class": "form-control",
        "type": "date"
    }))

    dangkynhantin = forms.BooleanField(label="Đăng ký nhận tin",  required=False)
