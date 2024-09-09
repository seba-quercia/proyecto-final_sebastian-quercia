from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Message, Profile

#Registro de usuarios
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        return username.lower()

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username'].lower()
        user.email = self.cleaned_data['email'].lower()
        if commit:
            user.save()
        return user

#Autenticacion de usuarios
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        return username.lower()

    def get_user(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Usuario o contraseña incorrectos")
        return user

# Actualizar datos de usuario
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 16:
            raise forms.ValidationError("El nombre de usuario no puede exceder los 16 caracteres.")
        return username.lower()

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()
        
#Cambio de contraseña
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )
    
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                self.add_error('new_password2', "Las contraseñas no coinciden.")
        return cleaned_data

#Actualizar avatar y biografia
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        
#Campos de mensajes
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body']
