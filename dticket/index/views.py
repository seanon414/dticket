from django.shortcuts import render


def home_screen(request):
    return render(request, 'templates/index.html', {})
