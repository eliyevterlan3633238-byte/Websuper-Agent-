from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Adınız və Soyadınız'), 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email ünvanınız'), 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Telefon nömrəniz')}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Mövzu'), 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Mesajınız'), 'rows': 5, 'required': True}),
        }
