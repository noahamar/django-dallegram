from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Dall•e•gram</h1>")
    return render(request, 'index.html')