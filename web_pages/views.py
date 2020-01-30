from django.shortcuts import render


# Create your views here.


def Home(request):
    return render(request, 'web_pages/home.html')


def About(request):
    return render(request, 'web_pages/about.html')


def Special_camp(request):
    return render(request, 'web_pages/special_camp.html')
