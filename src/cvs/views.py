from django.shortcuts import render


def cv_es(request):
    context = {}
    return render(request, 'cv_es.html', context)