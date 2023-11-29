from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'index.html')

def Login(request):
    return render(request,'login.html')