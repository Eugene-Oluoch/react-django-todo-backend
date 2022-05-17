from django.shortcuts import render
from .serializers import todoSerializer
from .models import todo
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class TodoSingle(APIView):
    def get(self,request, pk ,*args,**kwargs):
        toDo = todo.objects.get(id=pk)
        serializer = todoSerializer(toDo)
        return Response(serializer.data)

class TodoAll(APIView):
    def get(self,request,*args,**kwargs):
        todos = todo.objects.all()
        serializer = todoSerializer(todos,many=True)
        return Response(serializer.data)
    
    
class TodoAdd(APIView):
    def post(self,request,*args,**kwargs):
        serializer = todoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
        
class TodoUpdate(APIView):
    def patch(self,request,pk,*args,**kwargs):
        toDo = todo.objects.get(id=pk)
        serializer = todoSerializer(toDo, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
        
class TodoDelete(APIView):
    def delete(self,request,pk,*args,**kwargs):
        toDo = todo.objects.get(id=pk)
        toDo.delete()
        return Response('Delete successfully')