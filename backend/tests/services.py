from django.db.models import Model, QuerySet


def get_all_objects(model: Model) -> QuerySet:
    ''' return all elements of model'''

    return model.objects.all()
