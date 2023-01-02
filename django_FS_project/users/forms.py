from django import forms
# from django.contrib.auth.models import User  # user model table [auto created]
from django.contrib.auth.forms import UserCreationForm
from .models import User,Profile
from django.contrib import messages

# the user creation form saves only username and password, we want to add email for now [compitable with default user table]
# then we will add more when we add customer user table


# class UserRegisterForm(UserCreationForm):  # inherits from user creation form
#     email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')  # note that require=false if the field not reuires
#     first_name = forms.CharField(max_length=30, required=True)
#     last_name = forms.CharField(max_length=30, required=True)
#     gender = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     birthdate = forms.DateField()
#     nationality = forms.CharField(required=False)

#     class Meta:  # specifying the model we want the form to interact with
#         model = User
#         fields = ['username', 'email', 'password1', 'password2',
#                   'first_name', 'last_name', 'gender', 'birthdate', 'nationality']

# fields wanted in the form and in what order then in views: from .forms import UserRegisterForm and replace Usercreation in both form=.....

# new class for updates forms


class UserUpdateForm(forms.ModelForm):
    Username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:  # specifying the model we want the form to interact with
        model = User
        fields = ['username','password','email']
        #fields=['username']


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthdate = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'class': 'form-control'}))
    nationality = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:  # specifying the model we want the form to interact with
        model = Profile

        fields = ['first_name', 'last_name','gender', 'birthdate', 'nationality']



class ProfileRegisterForm(UserCreationForm): #inherits from user creation form
    email=forms.EmailField()  #note that require=false if the field not reuires 
    first_name=forms.CharField()
    last_name=forms.CharField()
    gender=forms.CharField()
    birthdate=forms.DateField()
    nationality=forms.CharField(required=False)

    class Meta:#specifying the model we want the form to interact with
        model=User
        fields=['username','email','password1', 'password2','first_name', 'last_name', 'gender', 'birthdate', 'nationality']
