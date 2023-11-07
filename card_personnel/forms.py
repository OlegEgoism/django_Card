from datetime import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from card_personnel.models import Personel, Contract, Registration, Education, LanguageSkills, Work, Family, Phone

def user_cap(name):
    if name.isupper():
        raise ValidationError('Имя с большой буквы')
    else:
        return


class PersonelForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget(years=range(1900, datetime.now().year)))

    class Meta:
        model = Personel
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = 'personel',


class ContractForm(forms.ModelForm):
    date_start = forms.DateField(label='Дата начала', widget=forms.SelectDateWidget(years=range(datetime.now().year, 2050)))
    date_end = forms.DateField(label='Дата окончания', widget=forms.SelectDateWidget(years=range(datetime.now().year, 2050)))

    class Meta:
        model = Contract
        exclude = 'personel',


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = 'personel',


class LanguageSkillsForm(forms.ModelForm):
    class Meta:
        model = LanguageSkills
        exclude = 'personel',


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        exclude = 'personel',


class FamilyForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.SelectDateWidget(years=range(1940, datetime.now().year + 1)))

    class Meta:
        model = Family
        exclude = 'personel',


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        exclude = 'personel',


class RegistrationUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = 'username', 'email', 'password1', 'password2',


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
