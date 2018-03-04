from django.shortcuts import render


def cv_es(request):
    context = {}
    return render(request, 'cv_es.html', context)

def cv_en(request):
    context = {}
    return render(request, 'cv_en.html', context)