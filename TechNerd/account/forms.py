from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# user register form
class UserRegisterForm(UserCreationForm):

    error_messages = {
        "password_mismatch":'گذرواژه ها منطبق نیستند',
    }

    username = forms.CharField(
        label="نام کاربری",
        max_length=150,
        help_text="اجباری, انگلیسی وارد کنید.",
        error_messages={
            'unique': 'این نام کاربری قبلا استفاده شده',
            'invalid': 'از کاراکتر های مجاز مثل @ , . , / استفاده کنید',
        }
    )
    email = forms.EmailField(
        label= "ایمیل",
        max_length=250,
        help_text= "اختیاری"
    )
    password1 = forms.CharField(
        label='گذرواژه',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='دست‌کم 8 نویسه وارد کنید',
        error_messages= {'password_too_short':'دست کم 8 نویسه وارد کنید',}
    )
    password2 = forms.CharField(
        label='گذرواژه',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text='باید گذرواژه را تکرارکنید',
        error_messages= {'password_too_short':'دست کم 8 نویسه وارد کنید',}
    )

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        if len(password2) < 8:
            raise forms.ValidationError(
                'دست کم 8 نویسه وارد کنید',
                code='password_too_short',
            )
        return password2


class UserLoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput,label='گذرواژه')
