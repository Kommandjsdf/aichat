from django import forms
from django.contrib.auth.forms import UserCreationForm


class PromptForm(forms.Form):
    prompt = forms.CharField(label="Enter your prompt", max_length=500, widget=forms.Textarea)

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         fields = ["username", "name", "surname", "password1", "password2"]