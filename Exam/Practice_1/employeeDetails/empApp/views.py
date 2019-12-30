from django.shortcuts import render
from django.views.generic import TemplateView
from empApp.models import Employee


# Create your views here.

class HomePage(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'home.html',context=None)

class DisplayPage(TemplateView):
    def get(self, request, **kwargs):
        usn = request.GET['usn']
        name = request.GET['name']
        addr = request.GET['addr']

        e = Employee(usn=usn, name=name, address=addr)

        e.save()

        elist = Employee.objects.all()

        return render(request, 'display.html', {'elist': elist})
