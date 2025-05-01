from rest_framework import serializers # type: ignore
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    description = serializers.CharField(allow_blank=False, min_length=3)
    due_date = serializers.DateTimeField(required=True, allow_null=False)
    is_completed = serializers.BooleanField(required=True)

    class Meta:
        model = Task
        fields = '__all__'

    def validate_description(self, value):
        if value.strip() == "":
            raise serializers.ValidationError("description field is cannot consist of only spaces characters.")
        return value