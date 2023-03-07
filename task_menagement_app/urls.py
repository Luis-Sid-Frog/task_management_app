from django.urls import path, include
from .import views
from rest_framework import routers
from task_menagement_app.views import *

urlpatterns = [
    # path('api/', views.appOverview, name='app-overview'),
    path('task-list/', TaskList.as_view()),
    path('task-detail/<int:pk>/', TaskDetail.as_view()),
    path('task-create/', TaskCreate.as_view()),
    path('task-delete/<int:pk>/', TaskDelete.as_view()),
    path('register/', CreateuserView.as_view())
]