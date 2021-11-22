from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        self.checkusername(self.cleaned_data['username'])
        self.checkpassword(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    # Checking if the password has the # character
    def checkpassword(self, password):
        if not any(char.isupper() for char in password) or "#" not in password:
            raise ValueError("Password has to contain at least 1 capital letter and a # character")
        else:
            pass

    def checkusername(self, username):
        special_string = re.compile('[@_.+-]')
        if special_string.search(username) is None:
            pass
        else:
            raise ValueError(f"Username can not contain special characters f{special_string}")
