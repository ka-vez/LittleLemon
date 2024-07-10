from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse('Hello David')

@api_view()
def items(request):
    return Response({"message" : "What's Up People"})

