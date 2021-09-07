from rest_framework import fields, serializers
from .models import Courses

class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("id","name", "description", "lecturer", "online","price",)
        model = Courses