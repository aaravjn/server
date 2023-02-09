import json

from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Lottery
from .serializers import ProfileSerializer, UserSerializer, LotterySerializer


@api_view(['GET'])
def profile_data(request):
    profile = request.user.profile
    data = {'name': profile.name, 'metamask_id': profile.metamask_id}
    return Response(data)


@api_view(['POST'])
def set_profile(request):
    serializer = ProfileSerializer(instance=request.user.profile, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response({'message': 'Invalid Data'})
    serializer.save()
    return Response({'message': 'Updated Successfully'})


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    if request.method != "POST":
        return Response({"message": "Method Not Allowed"})
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    if username is None or password is None:
        return Response({"message": "Authentication Failed"})
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"message": "Authentication Failed"})
    login(request, user)
    return Response({"message": "Logged In Successfully"})


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'message': 'Invalid Data'})
    serializer.save()
    return Response({'message': 'Registered Successfully'})


@api_view(['GET'])
def get_current_lottery(request):
    last = Lottery.objects.all().last()
    serialized = LotterySerializer(last)
    return Response(dict(serialized.data))


@api_view(['GET'])
def lottries_won(request):
    serialized = LotterySerializer(request.user.won_lotteries.all(), many=True)
    return Response(serialized.data)


@api_view(['POST'])
def register_in_lottery(request):
    last = Lottery.objects.all().last()
    last.participants.add(request.user)
    return Response({'message': "Successfully Registered"})


@api_view(['Get'])
def registered_lotteries(request):
    serialized = LotterySerializer(request.user.registered_lotteries.all(), many=True)
    return Response(serialized.data)
