from django import forms


class TempForm(forms.ModelForm):
    pass


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

    def clean_text(self):
        text = self.cleaned_data["text"]
        if "Temp" in text:
            raise forms.ValidationError("Temp is not allowed")
        return text
