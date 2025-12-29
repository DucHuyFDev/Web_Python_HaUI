from django import forms

NOT_ACCEPT_USERNAME = ['admin', 'root', 'test']

class SignUpForm(forms.Form):
    username = forms.CharField(label="Tên đăng nhập", widget=forms.TextInput({
        "placeholder": "Nhập tên đăng nhập"
    }))
    password = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput({
        
    }))
    confirm_password = forms.CharField(label="Xác nhận mật khẩu", widget=forms.PasswordInput({
        
    }))
    email = forms.CharField(label="Email", widget=forms.EmailInput({
        "placeholder": "Nhập email"
    }))

    def clean_username(self):
        username = self.cleaned_data["username"]
        if username.lower() in NOT_ACCEPT_USERNAME:
            raise forms.ValidationError("Không được đặt username này")
        return username
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.endswith('@student.edu.vn'):
            raise forms.ValidationError("Email sai định dạng")
        return email
    
    def clean(self): # ghi đè hàm clean() gốc
        cleaned_data = super().clean() # gọi clean() cha, để lấy toàn bộ data gốc
        pw = cleaned_data.get('password')
        cpw = cleaned_data.get('confirm_password')
        if pw and cpw and pw != cpw:
            self.add_error('confirm_password', "Mật khẩu không khớp")
