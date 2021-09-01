from django.core.paginator import Paginator


class ModelService:
    def __init__(self):
        pass

    # Creating model instance
    def create(self, **kwargs):
        obj = self.model(**kwargs)
        obj.save()

    # Getting list of model instances
    def get_list(self, **kwargs):
        queryset = self.model.objects
        if kwargs:
            queryset = queryset.filter(**kwargs)

        return queryset.all()
