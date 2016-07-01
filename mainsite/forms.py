import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import *

class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', required=True, max_length=30, widget=forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(required=True, max_length=30, widget=forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}), label=_("Email address"))
    password1 = forms.CharField(required=True, max_length=30, widget=forms.PasswordInput(attrs={'class':'inputfield w3-input w3-border'}), label=_("Password"))
    password2 = forms.CharField(required=True, max_length=30, widget=forms.PasswordInput(attrs={'class':'inputfield w3-input w3-border'}), label=_("Password (again)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data



class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('pic','name','branch','work','DOB','year','bio','linkedin','resume', 'active')
        labels = {
            'work':_('Place of Work'), 'DOB':_('Date of Birth'), 'bio':_('A little about Yourself'), 'linkedin':_('Your Linkedin Profile URL'),
        }
        help_texts = {
            'branch': _('Your current branch'), 'work':_('Keep empty if you are not employed somewhere.'), 'year':_('Your current Year, write like "First Year", or "Third Year", avoid all lowercase'),
            'bio':_('What you write will show a glimpse about you'), 'resume':_('Attach your Resume, you can upload it later also'), 'active':_('Tick if you are not Alumni'),
        }
        widget = {
            'name': forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}),
            'branch': forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}),
            'work': forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}),
            'DOB': forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}),
            'year': forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}),
            'bio': forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}),
            'linkedin': forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}),
            'resume': forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}),
            'active': forms.TextInput(attrs={'class':'inputfield w3-input w3-border'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        labels = {
            'pic':_('Project Picture'), 'name':_('Project Name'), 'github':_('Github Link'), 
        }
        help_texts = {
            'pic':_('If present'), 'github':_('If present'), 'completed':_('Tick if project is complete'), 'contributers':_('Write the names of Members who were involved in the project correctly.')
        }
        widget = {
            'pic': forms.TextInput(attrs={'class':'w3-input w3-border'}),
            'name': forms.TextInput(attrs={'class':'w3-input w3-border'}),
            'description': forms.TextInput(attrs={'class':'w3-input w3-border'}),
            'github': forms.TextInput(attrs={'class':'w3-input w3-border'}),
            'completed': forms.TextInput(attrs={'class':'w3-input w3-border'}),
            'contributers': forms.TextInput(attrs={'class':'w3-input w3-border'}),
        }


class ExpoProjectForm(forms.ModelForm):
    class Meta:
        model = ExpoProject
        fields = '__all__'
        