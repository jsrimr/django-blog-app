from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "사용자 이름")
    password = forms.CharField(label = "비밀번호",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "사용자 이름")
    password = forms.CharField(max_length=20,label = "비밀번호",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="비밀번호 확인",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다")

        values = {
            "username" : username,
            "password" : password
        }
        return values


