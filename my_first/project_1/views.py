from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    text='<h1> Welcome to My first Django app</h1>'
    return HttpResponse("I'M Happy that I learnt Basic of Django")