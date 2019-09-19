from django import forms


from .models import User


class LoginForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['phone_no', 'password']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'phone_no')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']