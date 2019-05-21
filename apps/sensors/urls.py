from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TemperatureViewSet


router = DefaultRouter()
router.register('sensors/temperature', TemperatureViewSet)


app_name = 'sensors'
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
