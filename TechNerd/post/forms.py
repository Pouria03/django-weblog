from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='')

class CommentForm(forms.Form):
    body = forms.CharField(label='',widget=forms.Textarea)
