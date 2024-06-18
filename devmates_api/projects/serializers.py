from rest_framework import serializers
from .models import *

class UserProjectSer(serializers.ModelSerializer):
    class Meta:
        model = UserProjects
        fields = '__all__'