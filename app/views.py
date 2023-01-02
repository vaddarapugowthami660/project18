from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'string':'chinni','list':[11,12,13],'tuple':(14,15,16)}
    return render(request,'looping.html',d)
