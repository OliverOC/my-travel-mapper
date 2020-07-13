from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = get_user_model()

        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'accounts-form-color'
        #     }),
        #     'note': forms.Textarea(attrs={
        #         'placeholder': 'Some things you remember...'
        #     }),
        #     'trip_img': forms.ClearableFileInput()
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['username'].label = 'Display Name'
        self.fields['username'].help_text = ' '
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].help_text = ' '


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('profile_pic',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_pic'].label = 'Profile Picture'


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['is_active'].label = 'Active'
        self.fields['is_active'].help_text = ' '
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'


class UpdateUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('profile_pic',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_pic'].label = 'Profile Picture'
