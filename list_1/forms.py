from django import forms

class Student_forms(forms.Form):
    student_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    roll_number = forms.IntegerField()
    