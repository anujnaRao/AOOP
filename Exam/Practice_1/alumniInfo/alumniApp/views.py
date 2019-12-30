from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'


class DisplayPage(TemplateView):
    def get(self, request, **kwargs):
        usn = request.GET['usn']
        name = request.GET['name']
        address = request.GET['addr']
        return render(request, 'display.html', {'USN': usn, 'Name': name, 'Address': address})
