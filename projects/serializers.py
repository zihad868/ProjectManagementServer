from rest_framework import serializers
from . models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Projects
        fields = ['id', 'name', 'description', 'owner', 'created_at']
    
    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['owner'] = request.user
        
        return super().create(validated_data)