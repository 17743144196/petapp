from django.http import HttpResponse,response,JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
def index(request):
    return HttpResponse('HELLO WORLD')


