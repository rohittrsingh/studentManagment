from django.urls import path
from .apis import SchoolView, StudentView, SchoolStudentView
from .views import school_register_view, student_register_view, school_edit_view

urlpatterns = [
    path('api/school/<int:id>', SchoolView.as_view()),
    path('api/student/<int:id>', StudentView.as_view()),
    path("api/all_schools_details", SchoolStudentView.as_view()),
    path("create_school", school_register_view),
    path("create_student",student_register_view),
    path("edit-school/<int:_id>", school_edit_view)
]
