from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'main/index.html'
    context = {}
    return render(request, template, context)
