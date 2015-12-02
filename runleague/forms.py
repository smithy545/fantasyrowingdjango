from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import League, User
from collections import OrderedDict

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
		super(ChooseLeagueForm, self).__init__(*args, **kwargs)
		openpks = [l.pk for l in League.objects.open_leagues()]
		self.fields = OrderedDict([('league',forms.ModelChoiceField(queryset=League.objects.filter(pk__in=openpks))),('teamname',self.fields['teamname'])])
		
class LeagueForm(forms.ModelForm):
	class Meta:
		model = League
		fields = ['name', 'size']

class TradePlayerForm(forms.Form):
	def __init__(self, user, *args, **kwargs):
		self.user = user
		super(TradePlayerForm, self).__init__(*args, **kwargs)
		self.fields['otherusers'] = forms.ChoiceField(label="Trade with", choices=[(u, u.username) for u in user.members.first().members.all()])
		self.fields['yourathletes'] = forms.MultipleChoiceField(label="Trade", choices=[(a,a) for a in user.team_set.first().athletes.all()])
		#self.fields['theirathletes'] = forms.MultipleChoiceField(label="For", choices=[(a,a) for a in user.members.first().athletes.all()])