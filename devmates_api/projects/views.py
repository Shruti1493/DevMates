from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.contrib.auth import authenticate
from .models import *

from rest_framework.permissions import IsAuthenticated


class CreateUserProject(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request, format=None):
        serializer = UserProjectSer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    def patch(self,request, format=None):
        try:
            
            serializer = UserProjectSer(request.user, data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User project does not exist'}, status=status.HTTP_404_NOT_FOUND)
