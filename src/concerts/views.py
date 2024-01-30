from django.shortcuts import render
from rest_framework import viewsets
from concerts.models import Concert
from concerts.serializers import ConcertSerializer


# Create your views here.
class ConcertViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Concert.objects.all()
    serializer_class = ConcertSerializer
