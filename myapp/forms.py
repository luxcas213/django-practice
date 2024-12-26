from django import forms

class createnewtask(forms.Form):
    title=forms.CharField(label="Title",max_length=200)
    description=forms.CharField(label="Description",widget=forms.Textarea)
    