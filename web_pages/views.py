from django.shortcuts import render
from .models import community_student


# Create your views here.


def Home(request):
    community_member = list(community_student.objects.all())
    community_list = []
    for member in zip(community_member[::2], community_member[::-2]):
        community_list.append(member)
    print(community_list)
    return render(request, 'web_pages/home.html', {'community_member': community_list})


def About(request):
    return render(request, 'web_pages/about.html')


def Special_camp(request):
    return render(request, 'web_pages/special_camp.html')
