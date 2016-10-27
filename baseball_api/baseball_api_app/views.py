from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetreiveUpdateDestroyAPIView

from baseball_api_app.models import Master, Batting, Pitching, Fielding
from baseball_api_app.serializers import MasterSerializer, BattingSerializer, PitchingSerializer, FieldingSerializer


class MasterListCreateAPIView(ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class MasterUpdateDestroyAPIView(RetreiveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class BattingListCreateAPIView(ListCreateAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer


class BattingUpdateDestroyAPIView(RetreiveUpdateDestroyAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer


class PitchingListCreateAPIView(ListCreateAPIView):
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer


class PitchingUpdateDestroyAPIView(RetreiveUpdateDestroyAPIView):
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer


class FieldingListCreateAPIView(ListCreateAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer


class FieldingUpdateDestroyAPIView(RetreiveUpdateDestroyAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer
