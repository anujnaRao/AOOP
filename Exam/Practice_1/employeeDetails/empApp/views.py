from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from empApp.models import Employee


# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'


class InsertPage(TemplateView):
    def get(self, request, **kwargs):
        usn = request.GET['usn']
        name = request.GET['name']
        addr = request.GET['addr']
        e = Employee(USN=usn, Name=name, Address=addr)
        e.save()
        return redirect('show')


def show(request):
    elist = Employee.objects.all()

    return render(request, 'display.html', {'elist': elist})
