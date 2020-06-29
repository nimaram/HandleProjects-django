from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز عبور',widget=forms.PasswordInput)
    password2 = forms.CharField(label='تایید رمز عبور',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','talents']
        labels = {
            'email' : 'ایمیل',
            'talents' : 'مهارت ها',
        }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('رمز عبور ها باید برابر و مساوی باشند')
        return cd['password2']
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit : 
            user.save()

class UserChangeForm(forms.ModelForm):
    password =  ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ['email','password','talents']
        labels = {
            'email' : 'ایمیل',
            'talents' : 'مهارت ها',
            'password' : 'رمز عبور',
        }
    def clean_password(self):
        return self.initial['password']    

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
class UserRegisteration(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    talents = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))       