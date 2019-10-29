from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)

    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)

    email = forms.EmailField(required=True, label='Email')

    # first_name = forms.CharField(max_length=200, required=False, label='first_name')

    def clean_password_confirm(self):

        password = self.cleaned_data.get("password")

        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

        return password_confirm

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        try:
            User.objects.get(first_name=None)
            raise ValidationError('This filed cant be empty.', code='firt_name_empty_filed')
        except User.DoesNotExist:
            return first_name

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user

    class Meta:

        model = User

        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']