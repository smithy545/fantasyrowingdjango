from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import League, User

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
	email = forms.EmailField(label="Email address", required=True, help_text="Required.")
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		
	def save(self, commit=True):
		user = super(SignupForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user

class ChooseLeagueForm(forms.Form):
	teamname = forms.CharField(max_length=100)
	def __init__(self, *args, **kwargs):
		super(self.__class__,self).__init__(*args, **kwargs)
		league = forms.ChoiceField(choices = [(l.pk,l) for l in League.objects.all() if len(l.members.all()) < l.leaguesize])
	
class NewLeagueForm(forms.Form):
	leaguename = forms.CharField(label='Title', max_length=100)
	leaguesize = forms.ChoiceField(label='Size', choices=[(6,6),(8,8),(10,10)])

class TradePlayerForm(forms.Form):
	otheruser = forms.ChoiceField(choices = ())