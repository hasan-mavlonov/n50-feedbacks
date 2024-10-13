from django.contrib.auth.hashers import check_password
from .models import StudentModel

class StudentModelBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            student = StudentModel.objects.get(username=username)
            if student and check_password(password, student.password):
                return student
        except StudentModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return StudentModel.objects.get(pk=user_id)
        except StudentModel.DoesNotExist:
            return None