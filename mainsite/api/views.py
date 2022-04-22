from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'DetailView': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': 'task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks)
    return Response(serializer.data)
