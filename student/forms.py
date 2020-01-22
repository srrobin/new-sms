from django import forms
from .models import StudentInfo, StudentDetailsInfo,StudentClassInfo,Session

class StudentSearchForm(forms.Form):
    student_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    roll =forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'class': 'form-control'}))
    session =forms.ModelChoiceField(required=False,queryset=Session.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))


class StudentInfoForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'})

        }


class StudentDetailForm(forms.ModelForm):

    class Meta:
        model = StudentDetailsInfo
        exclude = ('student',)

        widgets = {
            'roll_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'std_class': forms.Select(attrs={'class': 'form-control'}),
            'std_shift': forms.Select(attrs={'class': 'form-control'}),
            'std_section': forms.Select(attrs={'class': 'form-control'}),
            'std_session': forms.Select(attrs={'class': 'form-control'}),

        }



