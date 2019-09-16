from django.shortcuts import render
from django.json import JsonResponse

#  views here!

def home(request):
	return JsonResponse('')

def about(request):
	print("h1")
	return JsonResponse('')