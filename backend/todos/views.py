# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

from .models import Todo
from .serializers import TodoSerializer


class TodoUserWritePermission(BasePermission):
    message = 'Editing todos is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class ListTodo(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView, TodoUserWritePermission):
    permission_classes = [TodoUserWritePermission]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
