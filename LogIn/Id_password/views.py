from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def add(request):
    value1=int(request.POST['num1'])
    value2=int(request.POST['num2'])

    res=value1+value2


    return render(request,'result.html',{'result':res})