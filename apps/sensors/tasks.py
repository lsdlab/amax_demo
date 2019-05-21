from celery.decorators import task
from .serializers import TemperatureSerializer


@task(name="save_temperature")
def save_temperature(data):
    create_serializer = TemperatureSerializer(data=data)
    if create_serializer.is_valid(raise_exception=False):
        create_serializer.save()
        # return create_serializer.data
        return True
