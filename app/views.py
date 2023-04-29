from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'HAI HOw Are YoU'}
    return render(request,'filters.html',d)
