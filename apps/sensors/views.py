from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from .models import Temperature
from .serializers import TemperatureSerializer
from .tasks import save_temperature


class TemperatureViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    permission_classes = (AllowAny, )

    @action(
        methods=['post'],
        detail=False,
        url_path='celery_post',
        url_name='celery_post',
        serializer_class=TemperatureSerializer,
        permission_classes=[
            AllowAny,
        ])
    def celery_post(self, request):
        save_temperature.delay(request.data)
        # res = save_temperature.delay(request.data)
        # data = res.get()
        # return Response(data, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_201_CREATED)
