from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('service/',views.service,name='services'),
    path('news/',views.news,name='news'),
    path('thanks/',views.thanks,name="thanks"),
    path('contact/',views.contact,name="contact")
]
