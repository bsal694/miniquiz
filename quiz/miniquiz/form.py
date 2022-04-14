from django import forms
from .models import *

class question_form(forms.ModelForm):

    class Meta:
        model=Questions
        fields=['question']
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop("request")
    #     super(question_form, self).__init__(*args, **kwargs)
    #     self.fields["category"].queryset = Book.objects.filter(owner=self.request.user)

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request')
    #     super(question_form, self).__init__(*args, **kwargs)
    #     self.fields['category'].queryset = Category.objects.filter(
    #     uid=self.request.GET.get('category'))