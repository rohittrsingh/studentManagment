from django.forms import ModelForm
from .models import School, Student


class SchoolForm(ModelForm):

    class Meta:
        model = School
        fields = ["name"]


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ["name", "school"]

    def save(self, commit=True):
        student = super(StudentForm, self).save()
        student.enrolment = student.name[:2].upper() + str(student.id)
        if commit:
            student.save()
        return student
