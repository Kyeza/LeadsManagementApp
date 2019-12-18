from rest_framework import viewsets, permissions

from leads.models import Lead
from leads.serializers import LeadSerializer


class LeadsViewSet(viewsets.ModelViewSet):
    """
    API for creating, editing, viewing and deleting Leads
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [
        permissions.AllowAny
    ]
