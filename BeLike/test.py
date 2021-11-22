from django.test import TestCase
from api.forms import RegistrationForm


class RegistrationFormTestCase(TestCase):
    def setUp(self) -> None:
        self.form = RegistrationForm
        self.data = {
            "username": "marcos@",
            "email": "marcos@marcos.com",
            "password1": "marcosp#",
            "password2": "Marcosp#"
        }

    def test_checkusername(self):
        username = self.data["username"]
        t = self.form.check_username(self.form, username)

    def test_check_password(self):
        password = self.data["password1"]
        t = self.form.check_password(self.form, password)
