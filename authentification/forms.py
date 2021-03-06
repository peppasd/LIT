from django.forms import EmailField
from django import forms

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import password_validation


class UserCreationFormExtended(UserCreationForm): 
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )   

    class Meta:
        model = User
        fields = ("username", "email")    

class EditProfileForm(UserChangeForm):
    password= None
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )
    
    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class EditProfileFormInvalidEmail(EditProfileForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
        help_text=_("<div class='alert alert-danger'><strong>Entered email was wrong, email was not changed, please try again!</strong></div>")
    )