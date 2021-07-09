from django.shortcuts import render
from app.models import ClassMember  
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ClassMember.objects.all().order_by('-matric_number')
    serializer_class = UserSerializer



@api_view(['GET', 'POST'])
def users(request):
    queryset = ClassMember.objects.all().order_by('-matric_number')
    serializer = UserSerializer(queryset, many=True)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Created"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
    return Response(serializer.data)

@api_view([ 'PUT'])
def update_attendance(request, id):
    if request.method == 'PUT':
        queryset = get_object_or_404(ClassMember, id)
        queryset.attended = queryset.attended + 1
        queryset.save()
        return Response({"message": "User Updated"}, status=status.HTTP_201_CREATED)
