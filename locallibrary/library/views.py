from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main_page(request):
    return render(request, 'library/index.html')


def about(request):
    return render(request, 'library/about.html')


def contacts(request):
    return render(request, 'library/contacts.html')
