from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
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
	teamname = forms.CharField(label="Team name", max_length=100)
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
		self.fields['teams'] = forms.ChoiceField(label="Trade with", widget=forms.Select(attrs={'onchange':'get_athletes();'}), choices=[(u.team_set.first().id, u.team_set.first().name) for u in user.members.first().members.all() if u != self.user])
		self.fields['yourathletes'] = forms.MultipleChoiceField(label="Trade", choices=[(a,a) for a in user.team_set.first().athletes.all()])
		self.fields['theirathletes'] = forms.MultipleChoiceField(label="For", choices=[(a,a) for a in Athlete.objects.all()])

class EditNameForm(forms.Form):
	name = forms.CharField(label = "New name", max_length=100)