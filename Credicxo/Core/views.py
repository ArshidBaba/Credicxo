import re
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework import status
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics, permissions, mixins, authentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAdminUser
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, StudentSerializer, StudentDetailSerializer
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import Http404


#Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully. Now perform Login to get the Token",
        })

class StudentList(generics.ListCreateAPIView):
    authentication_classes = [authentication.SessionAuthentication, IsAuthenticated]
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    queryset = User.objects.filter(groups=2)
    serializer_class = StudentSerializer

    

class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class UserList(generics.ListCreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsSuperUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.owner == request.user
        else:
            return False
        # return super().has_object_permission(request, view, obj)

class UserDetailAPIView(generics.RetrieveAPIView):
    # permission_classes = (IsAuthenticated)
    # authentication_class = JSONWebTokenAuthentication

    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [IsOwner]
    queryset = User.objects.filter(groups=2)
    serializer_class = UserSerializer


    # # def get_queryset(self):
    # #     # user = User.objects.filter(username=self.request.user)
    # #     print(User.objects.filter(username=self.request.user))
    # #     user = User.objects.filter(username=self.request.user)
    # #     print(self.request.user)
    # #     # user = self.request.user
    # #     # print(user)
    # #     return 2
    # def get_object(self):
    #     queryset = self.get_queryset()
    #     filter = {}
    #     for field in self.multiple_lookup_fields:
    #         filter[field] = self.kwargs[field]

    #     obj = get_object_or_404(queryset, **filter)
    #     self.check_object_permissions(self.request, obj)
    #     return obj

    

