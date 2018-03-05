from django.shortcuts import render


def cv_es(request):
    path = request.get_full_path()
    context = { 'path' : path }
    return render(request, 'cv_es.html', context)

def cv_en(request):
    path = request.get_full_path()
    context = {'path': path}
    return render(request, 'cv_en.html', context)