from django import forms
from.models import blog,contactus

class blog_form(forms.ModelForm):
    class Meta:
        model = blog
        fields = "__all__"

class contact_form(forms.ModelForm):
    class Meta:
        model = contactus
        fields = "__all__"
