from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def trigger_error(request):
    division_by_zero = 1 / 0
