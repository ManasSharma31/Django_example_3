from django.shortcuts import render


def index(request):
    return render(request,'myfinal_app/index.html')

def other(request):
    return render(request,'myfinal_app/other.html')
