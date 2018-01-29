from django.shortcuts import render
from django.http import HttpResponse


def mysum(request, numbers):
    # request: HttpRequest
    result = sum(map(lambda s: int(s or 0), numbers.split('/')))
    return HttpResponse(result)
