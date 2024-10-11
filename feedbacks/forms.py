from django import forms
from django.contrib.auth.hashers import make_password
from .models import StudentModel


class StudentRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = StudentModel
        fields = ['full_name', 'username', 'email']

    # Validate that the two passwords match
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    # Override the save method to hash the password before saving
    def save(self, commit=True):
        student = super().save(commit=False)
        # Hash the password before saving
        student.password = make_password(self.cleaned_data["password1"])
        if commit:
            student.save()
        return student
