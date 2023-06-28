from django.shortcuts import render, get_object_or_404

from .forms import SchoolForm, StudentForm
from .models import School


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

    # school = get_object_or_404(School, id=_id)
    #
    # if request.method == 'GET':
    #     context = {'form': SchoolForm(instance=school), 'id': _id}
    #     return render(request, 'create_school.html', context)



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
