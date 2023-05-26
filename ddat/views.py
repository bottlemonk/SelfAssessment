from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def software_developer(request):
    template = loader.get_template('software_developer.html')
    return HttpResponse(template.render())

