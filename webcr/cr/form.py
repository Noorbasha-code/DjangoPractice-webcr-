from django import forms
from cr.models import Student1


class Student_info(forms.ModelForm):
    class Meta:
        model = Student1
        fields = "__all__"
