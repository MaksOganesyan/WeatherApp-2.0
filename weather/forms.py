# forms.py
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation
from .models import CustomUser

# Форма для регистрации
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'input-field'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    class Meta:
        model = CustomUser
        fields = ('email',)
        labels = {'email': 'Электронная почта'}
        widgets = {'email': forms.EmailInput(attrs={'class': 'input-field'})}

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        
        password_validation.validate_password(password1)
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# Форма для авторизации
class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Электронная почта", widget=forms.EmailInput(attrs={'class': 'input-field'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'input-field'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise forms.ValidationError("Пользователь с таким email не найден.")
        return email

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Неверный email или пароль.")
        return self.cleaned_data
