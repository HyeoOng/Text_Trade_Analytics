from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Animal
from .serializers import AnimalSerializer


class AnimalListApiView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        모든 Animal 목록을 표시
        '''
        animals = Animal.objects.all() # 모든 동물 데이터 가져오기
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        '''
        Animal을 하나 새로 만들기
        '''
        data = {
            'name': request.data.get('name'),
            'type': request.data.get('type'),
            'owner': request.user.id
        }
        serializer = AnimalSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class AnimalDetailApiView(APIView):

    def get(self, request, animal_id, *args, **kwargs):
        '''
        Animal id로 한 동물 데이터 요청
        '''
        animal  = Animal.objects.get(id=animal_id)
        serializer = AnimalSerializer(animal)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, animal_id, *args, **kwargs):
        '''
        Animal 삭제
        '''
        animal  = Animal.objects.get(id=animal_id)
        animal.delete()
        return Response(
            {"message": "Deleted!"},
            status=status.HTTP_200_OK
        )
