from django.shortcuts import render
from . models import Articles
# Create your views here.
def index(request):
    data = Articles.objects.all()
    context = {
        'data':data
    }
    return render(request,'index.html',context)

def details(request,pk):
    # pk = 1
    data1 = Articles.objects.get(id = pk)
    print(data1)
    context = {
        'data1' : data1
    }
    return render(request,'simple.html',context)
