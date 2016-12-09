from django.shortcuts import render


def index(request):
    return render(request, 'home.html', {'active': 'home'})
