import profile
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from app.models import *
from .serializers import *
from .pusher import pusher_client
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET','POST'])
def getData(request):
    if request.method=='GET':
        message = Message.objects.all()
        person = messageSerializer(message,many=True)
    if request.method == 'POST':
        person = messageSerializer(data=request.data)
        if person.is_valid():
            person.save()
            pusher_client.trigger('chat', 'message', {
                # "id":request.data['id'],
                'user':request.data['user'],
                'message':request.data['message'],
                'name':request.data['name'],
                'received':request.data['received'],
                'time':request.data['time'],
                'room':request.data['room'],
            })
    return Response(person.data)

@api_view(['GET','PUT'])
def updateRoomData(request,pk):
    try:
        message = Message.objects.get(id=pk)
    except message.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer = messageSerializer(message)
    if request.method == 'PUT':
        serializer = messageSerializer(message, data=request.data)  
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
    return Response(serializer.data)

@api_view(['POST','GET'])
def getRoomData(request):
    if request.method=='GET':
        rooms = Room.objects.all()
        serializer = roomSerializer(rooms,many=True)
    if request.method == 'POST':
        serializer = roomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)


@api_view(['GET','POST'])
def getUserData(request):
    if request.method == 'GET':
        profile = User.objects.all()
        serializer = userSerializer(profile,many=True)
    if request.method == 'POST':
        user = User.objects.create_user(username=request.data['username'],password=request.data['password'])
        print("user:",user)
        serializer = userSerializer(user)
        Profile.objects.create(user=user)
    return Response(serializer.data)

@api_view(['GET','PUT'])
def getProfileData(request,pk):
    if request.method == 'GET':
        profile = Profile.objects.get(user=pk)
        room = [{r.id,r.name} for r in profile.rooms.all()]
        # print("rooms:",rooms)
        serializer = profileSerializer(profile)
    if request.method=='PUT':
        profile = Profile.objects.get(user=request.data['user'])
        serializer = profileSerializer(profile, data=request.data)  
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)
    return Response(serializer.data)

@api_view(['POST',"GET"])
def createProfileData(request):
    if request.method == 'POST':
        serializer = profileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = profileSerializer(profile,many=True)
    return Response(serializer.data)
