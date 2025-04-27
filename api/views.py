from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer, UserSerializer
from .models import Note
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
def api_home_page(request):
   try:
      note_queryset = Note.objects.filter(author=request.user)
   except:
      return Response("ERROR",status=status.HTTP_400_BAD_REQUEST)
   if request.method == 'GET':
      note_queryset = Note.objects.all()
      serializeData = NoteSerializer(note_queryset, many=True).data
      return Response(serializeData)
      
   if request.method == 'POST':
      data = request.data
      serializeData = NoteSerializer(data=data)
      if serializeData.is_valid():
         serializeData.save()
         return Response(serializeData.data, status=status.HTTP_201_CREATED)
      return Response(serializeData.errors, status=status.HTTP_400_BAD_REQUEST)
         


@api_view(['GET','PUT', 'DELETE'])
def note_detail(request, pk):
   try:
      note = Note.objects.get(id=pk)
   except Note.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
      serializeData = NoteSerializer(note)
      return Response(serializeData.data, status=status.HTTP_200_OK)
   
   if request.method == 'PUT':
      data = request.data
      serializeData = NoteSerializer(note, data=data)
      if serializeData.is_valid():
         serializeData.save()
         return Response(serializeData.data, status=status.HTTP_201_CREATED)
      return Response(serializeData.errors, status=status.HTTP_400_BAD_REQUEST)

   if request.method == 'DELETE':
      note.delete()
      return Response('Successfully Delete', status=status.HTTP_204_NO_CONTENT)
   
class CreateUserView(generics.CreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [AllowAny]