from django.http import HttpResponse
from django.shortcuts import render

def versa(request):
	return render(request,'versa.html')

def reverse(request):
	text=request.GET['text']
	reversed_text = text[::-1]
	return render(request,'reverse.html',{'text':text,'revtext':reversed_text})