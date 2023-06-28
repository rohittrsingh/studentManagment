from rest_framework.generics import RetrieveAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from .models import School, Student
from .serializer import SchoolSerializer, StudentSerializer, SchoolStudentSerializer


class SchoolView(RetrieveAPIView):
    serializer_class = SchoolSerializer

    def get(self, *args, **kwargs):
        _id = kwargs.get('id')
        try:
            school = School.objects.get(pk=_id)
            serializer = self.serializer_class(school)
            return Response({"status": True, "message": "data generated successfully", "data": serializer.data})
        except School.DoesNotExist:
            return Response({"status": False, "message": "no school found", "data": "N/A"}, HTTP_404_NOT_FOUND)


class StudentView(RetrieveAPIView):
    serializer_class = StudentSerializer

    def get(self, *args, **kwargs):
        _id = kwargs.get('id')
        try:
            student = Student.objects.get(pk=_id)
            serializer = self.serializer_class(student)
            return Response({"status": True, "message": "data generated successfully", "data": serializer.data})
        except Student.DoesNotExist:
            return Response({"status": False, "message": "no student found", "data": "N/A"}, HTTP_404_NOT_FOUND)


class SchoolStudentView(ListAPIView):
    serializer_class = SchoolStudentSerializer
    queryset = School.objects.all()
