from rest_framework import serializers, reverse
from ..models import Job


class JobSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = ('title', 'description', 'salary', 'company_name',
                  'amount_of_jobs', 'contact', 'type_of_job', 'technologies', 'links',)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse.reverse('job-list-id', kwargs={'id': obj.pk}, request=request),
            'delete': reverse.reverse('job-list-id', kwargs={'id': obj.pk}, request=request),
            'update': reverse.reverse('job-list-id', kwargs={'id': obj.pk}, request=request),
        }

