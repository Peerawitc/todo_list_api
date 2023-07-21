from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
# api 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import WorklistSerializer
from todolistapp.models import Worklist
# Create your views here.
def index(request):
    return  HttpResponse("test")

@api_view(['GET'])
def getData(request): 
    worklist = Worklist.objects.all()
    serializer = WorklistSerializer(worklist,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addWork(request):
    serializer = WorklistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()

@api_view(['PUT'])
def edit(request):
    if "id" not in request.data:
        return JsonResponse({"error":"id not found"},400)
    worklist =  Worklist.objects.get(pk=request.data['id'])
    serializer  = WorklistSerializer(worklist,data=request.data,partial=True) #partial สำตัญมาก
    if serializer.is_valid():
        serializer.save()
    return Response()

@api_view(['DELETE','GET'])
def delete(request,id):
    try:
        worklist = Worklist.objects.get(pk=int(id))
        worklist.delete()
        return JsonResponse({"message":"success"},status=200)
    except Worklist.DoesNotExist:
        return  JsonResponse({"error":"id not found"},status=400)

@api_view(['GET'])
def detail(request,id):
    worklist = Worklist.objects.get(pk=id)
    serializer = WorklistSerializer(worklist)
    return Response(serializer.data)

