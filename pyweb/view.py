from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def exam(request):
    return render(request, 'exam.html')


def sure(request):
    return render(request, 'sure.html')

