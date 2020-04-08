from django.http import Http404

from ..models import Technology


def list_technologies():
    techs = Technology.objects.all()
    return techs


def insert_technologies(tech):
    return Technology.objects.create(name=tech.name)


def list_technologies_id(id):
    try:
        return Technology.objects.get(id=id)
    except Technology.DoesNotExist:
        raise Http404


def update_technologies(technology_before_update, new_tech):
    technology_before_update.name = new_tech.name
    technology_before_update.save(force_update=True)


def remove_technologies(tech):
    tech.delete()