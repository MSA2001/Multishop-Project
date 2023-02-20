from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your email'}),
            'title': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'text': forms.Textarea(attrs={'placeholder': 'Message'})
        }

