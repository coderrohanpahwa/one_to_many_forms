from django import forms
from .models import Answer
from django.contrib.auth.models import User
class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = '__all__'
        def save(self, commit=True):
            instance = super().save(commit)
            # set Car reverse foreign key from the Person model
            instance.car_set.add(self.cleaned_data['ans'])
            return instance