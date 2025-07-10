from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class TempForm(forms.ModelForm):
    pass


phone_validator = RegexValidator(
    regex=r"^\+7 \d{3} \d{3} \d{2} \d{2}$", message="Phone number must be 10 digits"
)


class TempForm(forms.Form):
    email = forms.EmailField(
        label="Email Talaasy",
        max_length=50,
        widget=forms.EmailInput(
            attrs={"placeholder": "email_name@example.com", "maxlength": "50"}
        ),
    )

    text = forms.CharField(
        label="Text Talaasy",
        max_length=20,
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Enter your feedback "}),
    )

    phone_number = forms.CharField(
        label="Phone Number", validators=[phone_validator], required=False
    )

    def clean_text(self):
        text = self.cleaned_data["text"]
        if "Temp" in text:
            raise forms.ValidationError("Temp is not allowed")
        return text

    def clean_email(self):
        data = self.cleaned_data["email"]

        if not "@gmail.com" in data:
            raise forms.ValidationError("Email only @gmail.com It must be")
        return data


class UserRegisterForm(forms.ModelForm):
    # password
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Пароль кайра киргиз", widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
    def clean_password2(self):
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("Passwords don't match")
        else:
            return self.cleaned_data["password"]


class UserLoginForm(forms.ModelForm):

    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "password"]

#  sabak_42