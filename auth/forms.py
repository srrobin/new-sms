from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={"class":'form-control','placeholder':'Enter Emails'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Frist Name'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
        self.fields['username'].label=''
        self.fields['username'].help_text=''

        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
        self.fields['password1'].label=''
        self.fields['password1'].help_text=''

        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Con-Password'})
        self.fields['password2'].label=''
        self.fields['password2'].help_text=''


class EditRegisterForms(UserChangeForm):
    email = forms.EmailField(label = "", widget= forms.TextInput(attrs={"class":"form-control","placeholder":"Email Address"}))
    first_name = forms.CharField(label= "",max_length=100,widget= forms.TextInput(attrs={"class":"form-control","placeholder":"First Name"}))
    last_name = forms.CharField(label= "",max_length=100,widget= forms.TextInput(attrs={"class":"form-control","placeholder":"Lase Name"}))
    password = forms.CharField(label = "", widget= forms.TextInput(attrs={"type":"hidden"}))
    class Meta:
        model =User
        fields = ("username", "first_name", "last_name", "email", "password",)

    def __init__(self,*args,**kwargs):
        super(EditRegisterForms, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({"class":"form-control","placeholder":"User Name"})
        self.fields['username'].label=""
        self.fields['username'].help_text = ''