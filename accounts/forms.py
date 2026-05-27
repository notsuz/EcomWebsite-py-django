from django import forms
from .models import Profile
from datetime import datetime, timedelta

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_picture", "bio", 'dob']
        
        
        widgets={
            'dob':forms.DateInput(attrs={'type':'date', 'max':(datetime.now()-timedelta(days=36000)).strftime("%Y-%m-%d")})
        }