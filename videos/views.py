from django.shortcuts import render

# Create your views here.


def show_animeTv(request):
    return render(request, 'index.html')


def show_new(request):
    return render(request, 'new.html')
