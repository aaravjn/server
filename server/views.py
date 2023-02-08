import json

from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import ProfileSerializer, UserSerializer


@api_view(['GET'])
def xyz(request):
    profile = request.user.profile
    data = {'name': profile.name, 'metamask_id': profile.metamask_id}
    return Response(data)


@api_view(['POST'])
def set_profile(request):
    serializer = ProfileSerializer(instance=request.user.profile, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response({'message': 'Invalid data'})
    serializer.save()
    return Response({'message': 'Updated Successfully'})


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def api_login(request):
    if request.method != "POST":
        return Response({"message": "Method Not Allowed"})
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    if username is None or password is None:
        return Response({"message": "authentication failed"})
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"message": "authentication failed"})
    login(request, user)
    return Response({"message": "logged in successfully"})


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'message': 'Invalid data'})
    serializer.save()
    return Response({'message': 'Registered Successfully'})
