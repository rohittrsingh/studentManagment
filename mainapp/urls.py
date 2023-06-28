from django.urls import path
from .apis import SchoolView, StudentView, SchoolStudentView
from .views import school_register_view, student_register_view, school_edit_view, school_delete_view, \
    student_delete_view, student_list, school_list

urlpatterns = [
    path('api/school/<int:id>', SchoolView.as_view()),
    path('api/student/<int:id>', StudentView.as_view()),
    path("api/all_schools_details", SchoolStudentView.as_view()),
    path("create_school", school_register_view),
    path("create_student", student_register_view),
    path("edit-school/<int:_id>", school_edit_view),
    path("delete_student/<int:_id>", student_delete_view),
    path("delete_School/<int:_id>", school_delete_view),
    path("student_list",student_list),
    path("school_list",school_list)
]
