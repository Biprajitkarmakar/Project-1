from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm , UserChangeForm , SetPasswordForm
from . models import CustomUser , Booking


class MyRegFrm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username', 'first_name', 'last_name', 'email', 'mobile' , 'city_town_village' , 'street_name' , 'pin_code')
        labels = {
            'city_town_village': "City/Town/Village",
        }
        
class EditProfileForm(UserChangeForm):
    password = None  
    username = None
    email = None
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','mobile',
                  'street_name', 'city_town_village', 'pin_code')
        labels = {
            'city_town_village': "City/Town/Village",
        }        
        help_texts = {
            'username': None, 
        }
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone', 'service_type', 'booking_date', 'message']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 100%; height: 150px; resize: vertical;'}),
        }        
        
class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''  # Remove help text        