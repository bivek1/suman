from django import forms
from .models import Staff, Student
class StaffForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 200, label="First Name", widget= forms.TextInput(attrs = {'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length = 200, label="Last Name", widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Last Name'}) )
    username = forms.CharField(max_length = 200, label="Username", widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Username'}) )
    password = forms.CharField(max_length = 200, label="Password", widget=forms.PasswordInput(attrs = {'class':'form-control', 'placeholder':'Password'}) )
    class Meta:
        model = Staff
        fields = ('number', 'Temporary_address' , 'gender')
        
        labels = {
            'number': 'Number', 
            'Temporary_address': 'Address', 
            'gender': 'Gender'
        }
        widgets = {
            'number': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'Number'}), 
            'Temporary_address': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Address'}), 
            'gender': forms.Select(attrs = {'class':'form-control', 'placeholder':'Gender'})
        }
    
    
class StudentForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 200, label="First Name", widget= forms.TextInput(attrs = {'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length = 200, label="Last Name", widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Last Name'}) )
    email = forms.EmailField(max_length = 200, label="Parent Email", widget=forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Email'}) )
    class Meta:
        model = Student
        fields = ('number','id_card', 'faculty', 'Temporary_address', 'street', 'district' , 'gender')
        labels = {
            'faculty': 'Faculty',
            'number': 'Parents Number', 
            'id_card':'ID Card No.',
            'Temporary_address': 'City', 
            'street': 'Street Address', 
            'district': 'District' , 
            'gender': 'Gender'
        }
        widgets = {
            'faculty':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Faculty'}), 
            'number': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'Number'}), 
            'Temporary_address': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'City'}), 
            'street': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Street Address'}), 
            'district': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'District'}), 
            'gender': forms.Select(attrs = {'class':'form-control', 'placeholder':'Gender'}),
            'id_card': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'ID CARD NO.'}), 
        }