from django.conf.urls import url
from django.urls import path, include
from .views import RegisterAPI, StudentList, UserList, UserDetailAPIView
urlpatterns = [
      path('api/register/', RegisterAPI.as_view()),
      path('api/studentlist/', StudentList.as_view()),
      path('api/userlist/', UserList.as_view()),
      path('api/userdetail/<int:pk>/', UserDetailAPIView.as_view())
]