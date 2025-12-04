from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/todos/   -> list all todos
    POST /api/todos/   -> create a new todo
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/todos/<id>/ -> get one todo
    PUT    /api/todos/<id>/ -> update
    PATCH  /api/todos/<id>/ -> partial update
    DELETE /api/todos/<id>/ -> delete
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
