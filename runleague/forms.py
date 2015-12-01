from django import forms
from .models import League

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class SignupForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)
	email = forms.CharField(max_length=100)

class ChooseLeagueForm(forms.Form):
	teamname = forms.CharField(max_length=100)
	def __init__(self, *args, **kwargs):
		super(self.__class__,self).__init__(*args, **kwargs)
		league = forms.ChoiceField(choices = [(l.pk,l) for l in League.objects.all() if len(l.members.all()) < l.leaguesize])
	
class NewLeagueForm(forms.Form):
	leaguename = forms.CharField(label='Title', max_length=100)
	leaguesize = forms.ChoiceField(label='Size', choices=[(6,6),(8,8),(10,10)])