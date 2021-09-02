class CoreRepository:
    model = None

    def __init__(self):
        pass

    # Getting queryset of model
    def get_queryset(self):
        return self.model.objects

    # Getting list of model instances
    def get_list(self, **kwargs):
        queryset = self.get_queryset()
        if kwargs:
            queryset = queryset.filter(**kwargs)

        return queryset.all()

    # Getting model instance
    def get(self, **kwargs):
        return self.get_queryset().get(**kwargs)

    # Creating model instance
    def create(self, **kwargs):
        obj = self.model(**kwargs)
        obj.save()

    # Updating model instance
    def update(self, instance_id, **kwargs):
        return self.get_queryset().filter(id=instance_id).update(**kwargs)
