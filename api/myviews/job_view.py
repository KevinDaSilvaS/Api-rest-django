from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.serializers import job_serializer
from api.services import job_service
from api.entities import job


class JobList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        pagination = LimitOffsetPagination()
        jobs = job_service.list_jobs()
        result = pagination.paginate_queryset(jobs, request)
        serializer = job_serializer.JobSerializer(result, context={'request': request}, many=True)
        return pagination.get_paginated_response(serializer.data)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = job_serializer.JobSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            description = serializer.validated_data['description']
            salary = serializer.validated_data['salary']
            company_name = serializer.validated_data['company_name']
            amount_of_jobs = serializer.validated_data['amount_of_jobs']
            contact = serializer.validated_data['contact']
            type_of_job = serializer.validated_data['type_of_job']
            technologies = serializer.validated_data['technologies']

            new_job = job.Job(title=title, description=description, salary=salary,
                              company_name=company_name, amount_of_jobs=amount_of_jobs,
                              contact=contact, type_of_job=type_of_job, technologies=technologies)
            db_job = job_service.insert_jobs(new_job)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobListDetail(APIView):
    def get(self, request, id, format=None):
        job = job_service.list_jobs_id(id)
        serializer = job_serializer.JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        job_before_update = job_service.list_jobs_id(id)
        serializer = job_serializer.JobSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.data['title']
            description = serializer.data['description']
            salary = serializer.data['salary']
            company_name = serializer.data['company_name']
            amount_of_jobs = serializer.data['amount_of_jobs']
            contact = serializer.data['contact']
            type_of_job = serializer.data['type_of_job']
            technologies = serializer.data['technologies']
            new_job = job.Job(title=title, description=description, salary=salary,
                              company_name=company_name, amount_of_jobs=amount_of_jobs,
                              contact=contact, type_of_job=type_of_job, technologies=technologies)
            job_service.update_jobs(job_before_update, new_job)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        job = job_service.list_jobs_id(id)
        job_service.remove_jobs(job)
        return Response({'response': 'register succesfully removed'}, status=status.HTTP_204_NO_CONTENT)
