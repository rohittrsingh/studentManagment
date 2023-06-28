from django.db import models


class DateTimeBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class School(DateTimeBaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Student(DateTimeBaseModel):

    name = models.CharField(max_length=250)
    enrolment = models.CharField(max_length=10, unique=True, blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="school_student")

    def __str__(self):
        return self.name
