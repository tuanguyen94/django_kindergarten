from django.http import HttpResponse
from django.shortcuts import render

from kidGames.models import question

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    mystring = "this is a string"
    data = question.objects.all();
    return render(request,"home.html",{ "data": data})