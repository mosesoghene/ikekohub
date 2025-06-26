from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import StudentProfile, TeacherProfile, AdminProfile, UserRole
from .permissions import (
    IsAdmin, IsTeacher, IsStudent, IsAdminOrTeacher,
    IsOwnerOrAdminOrTeacher, IsStudentOwnerOrParentOrTeacher
)
from .serializers import AdminProfileSerializer


# Admin-only view
class AdminDashboardView(generics.GenericAPIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome to admin dashboard"})
