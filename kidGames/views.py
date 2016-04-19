from django.http import HttpResponse
from django.shortcuts import render

from kidGames.models import question

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    mystring = "this is a string"
    data = question.objects.all();
    return render(request,"home.html",{ "data": data})

def k5(request):
    data = question.objects.filter(category_id=5)[0];
    return render(request,"table.html",{"data": data})

def k6(request):
    data = question.objects.filter(category_id=6)[0];
    return render(request,"k6.html",{"data": data})

def k7(request):
    data = question.objects.filter(category_id=7)[0];
    return render(request,"k7.html",{"data": data})

def k8(request):
    data = question.objects.filter(category_id=8)[0];
    return render(request,"k8.html",{"data": data})


def l1(request):
    data = question.objects.filter(category_id=1)[0];
    return render(request,"l1.html",{"data": data})

def l2(request):
    data = question.objects.filter(category_id=2)[0];
    return render(request,"l2.html",{"data": data})


def checkAnsweer(request):
	category_Id = request.POST["category_id"];
	question_Number = request.POST["question_number"];
	ansWeer = request.POST["answeer"];
	data = question.objects.filter(category_id=int(category_Id))[int(question_Number)-1];
	if (int(ansWeer) == int(data.answeer)):
		return render(request,"result.html",{"data": "Good job kid"})
	else:
		return render(request,"result.html",{"data": "Try hard more baby"})
