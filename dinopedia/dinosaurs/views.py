from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Dinosaur
from .serializers import DinosaurSerializer


@csrf_exempt
def dinosaurs_list(request):
    if request.method == "GET":
        dinosaurs = Dinosaur.objects.all()
        serializer = DinosaurSerializer(dinosaurs, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
def dinosaur_detail(request, pk):
   
    try:
        dinosaur = Dinosaur.objects.get(pk=pk)
    except Dinosaur.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = DinosaurSerializer(dinosaur)
        return JsonResponse(serializer.data, status=200)
    