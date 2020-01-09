from django.urls import path
from . import views

urlpatterns = [
       path('',views.Home,name='home'),
       path('about/',views.About ,name='about'),
       path('special_camp/',views.Special_camp ,name='special-cap'),         
]