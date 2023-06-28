from django.shortcuts import render, get_object_or_404

from .forms import SchoolForm, StudentForm
from .models import School, Student


def school_register_view(request):
    if request.method == "POST":
        school_form = SchoolForm(request.POST)
        if school_form.is_valid():
            school_form.save()
            return render(request, "submitted.html")
        else:
            return render(request, "error.html")
    else:
        form = SchoolForm()
        return render(request, "create_school.html", {"form": form})


def student_register_view(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return render(request, "submitted.html")
        else:
            return render(request, "error.html")
    else:
        form = StudentForm()
        return render(request, "create_school.html", {"form": form})


################################################## EDIT ########################################

def school_edit_view(request, _id):
    try:
        school = School.objects.get(pk=_id)
    except School.DoesNotExist:
        return render(request, "404.html")

    if request.method == "POST":
        school_form = SchoolForm(request.POST, instance=school)
        if school_form.is_valid():
            school_form.save()
            return render(request, "submitted.html")
        else:
            return render(request, "error.html")
    else:
        form = SchoolForm(instance=school)
        return render(request, "create_school.html", {"form": form})


def student_edit_view(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return render(request, "submitted.html")
        else:
            return render(request, "error.html")
    else:
        form = StudentForm()
        return render(request, "create_school.html", {"form": form})


def student_delete_view(request, _id):
    student = Student.objects.get(id=_id)
    student.delete()
    return render(request, "submitted.html")


def school_delete_view(request, _id):
    school = School.objects.get(id=_id)
    school.delete()
    return render(request, "submitted.html")


def get_student_view(request, _id):
    student = Student.objects.get(id=_id)
    return render(request, "submitted.html")