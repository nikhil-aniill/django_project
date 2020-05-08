from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import MemberSerializer, mainclassserializer
from .models import Member ,Main_class#,Period
class MemberViewSet(viewsets.ModelViewSet):
    #queryset = Member.objects.all()
    queryset = Main_class.objects.all()
    serializer_class = mainclassserializer
    #serializer_class = MemberSerializer
        