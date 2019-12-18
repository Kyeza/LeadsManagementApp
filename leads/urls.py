from django.urls import path, include
from rest_framework import routers

from leads import api

router = routers.DefaultRouter()
router.register(r'leads', api.LeadsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
