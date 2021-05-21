from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Mark,Schedule,Addon,DefaultList,DueList,HostelAllot,LoanList
from django.core import validators

def validate_marks(value):
    if value<0:
        raise forms.ValidationError("Enter valid marks.")

def validate_amount(value):
    if value<0:
        raise forms.ValidationError("Enter a valid amount.")

def validate_day(value):
    if value not in ['MONDAY' , 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']:
        raise forms.ValidationError("Enter a valid day")

def validate_type(value):
    if value not in ['LECTURE' , 'TUTORIAL', 'LAB']:
        raise forms.ValidationError("Enter a valid schedule type")

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class MarkForm(forms.ModelForm):

    score= forms.IntegerField(validators=[validate_marks])
    class Meta:
        model = Mark
        fields = "__all__"

class ScheduleForm(forms.ModelForm):
    day=forms.CharField(validators=[validate_day])
    type=forms.CharField(validators=[validate_type])
    class Meta:
        model = Schedule
        fields = "__all__"

class AddonForm(forms.ModelForm):
    class Meta:
        model = Addon
        fields = "__all__"

class DefaultForm(forms.ModelForm):
    amount=forms.IntegerField(validators=[validate_amount])
    class Meta:
         model = DefaultList
         fields = "__all__"

class DueForm(forms.ModelForm):
    amount=forms.IntegerField(validators=[validate_amount])
    class Meta:
         model = DueList
         fields = "__all__"

class HostelForm(forms.ModelForm):
    class Meta:
        model = HostelAllot
        fields = "__all__"

class LoanForm(forms.ModelForm):
    class Meta:
        model = LoanList
        fields = "__all__"
