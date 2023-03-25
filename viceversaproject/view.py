from django.http import HttpResponse
from django.shortcuts import render

def versa(request):
	return render(request,'versa.html')