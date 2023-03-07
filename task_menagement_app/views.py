from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer, UserSerializer
from rest_framework.response import Response
from .models import Task
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model


# @api_view()
# def appOverview(request):
#     api_urls = {
#         'List':'/task-list/',
#         'Detail View': '/task-detail/<str:pk>/',
#         'Create': '/task-create/',
#         'Update': '/task-update/<str:pk>/',
#         'Delete': '/task-delete/<int:pk>/',
#     }

#     return Response(api_urls)

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status','id','title','description',]
    

class TaskDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

class TaskCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateuserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer