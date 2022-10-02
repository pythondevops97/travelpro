from django.shortcuts import render
from .models import Place, teams


# Create your views here.
def index(request):
    obj = Place.objects.all()
    obj1 = teams.objects.all()

    return render(request,'index.html',{'result':obj,'result1':obj1})
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')
def news(request):
    return render(request,'news.html')
def contact(request):
    return render(request,'contact.html')
def thanks(request):
    return render(request,'thanks.html')