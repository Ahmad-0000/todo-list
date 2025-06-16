from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    """
    Index page
    """
    return HttpResponse('Hello user')
