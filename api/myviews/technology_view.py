from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.serializers import technology_serializer
from api.services import technology_service
from api.entities import technology


class TechnologyList(APIView):

    def get(self, request, format=None):
        technologies = technology_service.list_technologies()
        serializer = technology_serializer.TechnologySerializer(technologies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = technology_serializer.TechnologySerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data['name']
            new_tech = technology.Technology(name=name)
            db_tech = technology_service.insert_technologies(new_tech)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechnologyListDetail(APIView):
    def get(self, request, id, format=None):
        technologies = technology_service.list_technologies_id(id)
        serializer = technology_serializer.TechnologySerializer(technologies)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        technology_before_update = technology_service.list_technologies_id(id)
        serializer = technology_serializer.TechnologySerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data['name']
            new_tech = technology.Technology(name=name)
            technology_service.update_technologies(technology_before_update, new_tech)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        technologies = technology_service.list_technologies_id(id)
        technology_service.remove_technologies(technologies)
        return Response({'response': 'register succesfully removed'}, status=status.HTTP_204_NO_CONTENT)
