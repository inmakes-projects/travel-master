from django.shortcuts import render
from .models import Destination, Member

# Create your views here.

def index(request):
    destinations = Destination.objects.all()
    members = Member.objects.all()
    context = {
        'destinations': destinations,
        'members': members
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'sevices.html')
