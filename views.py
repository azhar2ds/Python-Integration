from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class GetInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class PostInput(View):
    def get(self,request):
        return render(request, 'postinput.html')
class Add(View):
    def get(self,request):
        try:
            a=request.GET['t1']
            v=int(a)
            b=request.GET['t2']
            w=int(b)
            c=request.GET['t3']
            x=int(c)
            d=request.GET['t4']
            y=int(d)
            z=v+w+x+y
            return HttpResponse("<html><body bgcolor=red><h1>sum is:"+str(z)+"</h1></body></html>")
        except(ValueError):
            return HttpResponse("invalid input")
    def post(self, request):
        try:
            a=request.POST['t1']
            v=int(a)
            b=request.POST['t2']
            w=int(b)
            c=request.POST['t3']
            x=int(c)
            d=request.POST['t4']
            y=int(d)
            z=v+w+x+y
            return HttpResponse("<html><body bg color=red><h1>sum is:" +str(z)+ "</h1></body></html>")
        except(ValueError):
            return HttpResponse("invalid Input")

