from django import forms

class StudentForm(forms.Form):
   firstname=forms.CharField(label="Enter First Name",max_length=50)
   lastname=forms.CharField(label="Enter Last Name",max_length=50)
   email=forms.EmailField(label="Enter Email")
   file=forms.FileField()



