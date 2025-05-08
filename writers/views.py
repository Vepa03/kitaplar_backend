from rest_framework import viewsets

from .serializers import WriterListSerializer, WriterRetrieveSerializer
from .models import Writer


class WriterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Writer.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return WriterRetrieveSerializer
        return WriterListSerializer