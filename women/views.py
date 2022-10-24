from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('Main Page!')


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Page of categories!<p>{catid}</p>')


def archive(request, year):
    return HttpResponse(f'Page of year!<p>{year}</p>')