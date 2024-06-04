from django.shortcuts import render
from rest_framework import generics
from .models import ListFeatures
from .serializers import ListFeaturesSerializer

class ListFeaturesList(generics.ListCreateAPIView):
    serializer_class = ListFeaturesSerializer

    def get_queryset(self):
        queryset = ListFeatures.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset

class ListFeaturesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ListFeaturesSerializer
    queryset = ListFeatures.objects.all()