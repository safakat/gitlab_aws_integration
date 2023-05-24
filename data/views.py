from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class HomeView(APIView):
    def get(self,request):
        return JsonResponse({'HELLO':'WORLD'},status = 200)
    def post(self,request):
        pass
