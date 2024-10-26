from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def Clientsection(request):
    return render(request,'Clientsection.html')