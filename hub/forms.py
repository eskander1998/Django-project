from unicodedata import name
from django import forms
from .models import Coach, Student 


class CoachForm(forms.Form):
    first_name=forms.CharField(
        label='Prenom',max_length=80
    )
    name=forms.CharField(
        label='nom',max_length=80
    )
    email=forms.EmailField()

class CoachModelForm( forms.ModelForm):
    class Meta:
        model = Coach 
        fields= '__all__'
        errors_message= {
            'last_name' : {
                'max_length' : " Name too long !!"
            }
        }

class StudentModelForm( forms.ModelForm):
    class Meta:
        model = Student 
        fields= '__all__'
        errors_message= {
            'last_name' : {
                'max_length' : " Name too long !!"
            }
        }


