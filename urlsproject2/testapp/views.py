from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobsinfo(request):
    s ='<h1> hyderabad jobs information</h1>'
    return HttpResponse(s)
def punejobsinfo(request):
    s ='<h1> pune jobs information</h1>'
    return HttpResponse(s)
def mumbaijobsinfo(request):
    s ='<h1> mumbai jobs information</h1>'
    return HttpResponse(s)
def noidajobsinfo(request):
    s ='<h1> noida jobs information</h1>'
    return HttpResponse(s)