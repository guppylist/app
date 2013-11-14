from django import forms

class ListForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'List Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'My shoe size is 8 and I like the blue ones.'}))