from django.shortcuts import render
from myapp.models import DeviceCoverage,Categories,Device
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request,'index.html')

def Store(request):
    cat = Categories.objects.all()  
    data = {
        "categories":cat
    }
    return render(request,'store.html',data)

@csrf_exempt
def Services(request):
    if(request.method=='POST'):
        serial = request.POST.get("serial")
        model = DeviceCoverage(serial=serial)
        model.save()
    return render(request,'services.html')

def shop(request,device):
    data = Device.objects.filter(model=device)
    if data:
        context = {
        'device':device,
        'data':data
        }
        return render(request,'shop.html',context)
    else:
        return HttpResponse('No Data Found !')
    
def Signin(request):
    return render(request,'signin.html')