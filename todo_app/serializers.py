from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer turns Todo model instances into JSON and
    validates JSON data coming from the client to create/update Todos.
    """
    class Meta:
        model = Todo
        # Fields that will appear in the API response
        fields = ['id', 'title', 'completed', 'created_at']
