from django.shortcuts import render
from .models import*
# Create your views here.
def home(request):
    list_proj=Property.objects.all()
    return render(request,'home.html',{'properties':list_proj})
