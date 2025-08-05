from django import forms
from django.contrib.auth.models import User


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'block bg-gray-700 border text-sm md:text-xl w-sm md:w-lg py-2 px-2'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'block bg-gray-700 border text-sm md:text-xl w-sm md:w-lg py-2 px-2'}))

    class Meta:
        model = User
        fields = ['username','email', 'password']
        widgets = {
            'username':forms.TextInput(attrs={'class':' block bg-gray-700 border text-sm md:text-xl w-sm md:w-lg py-2 px-2'}),
            'email':forms.EmailInput(attrs={'class':'block bg-gray-700 border text-sm md:text-xl w-sm md:w-lg py-2 px-2', 'placeholder': 'Email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # 🔐 Hash the password
        if commit:
            user.save()
        return user