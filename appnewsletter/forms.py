from django import forms

from .models import NewsLetterEmail


class EmailForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetterEmail
        fields = "__all__"