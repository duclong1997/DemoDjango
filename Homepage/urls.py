from django.urls import path
from . import views

urlpatterns =[
    #  when call urls of Homepage -> link ''-> cass function show in views
    # path : name link url
    path('long/', views.show),
    path('test/',views.showtest),
    path('homepage/',views.showPage),
    path('contact/',views.showContact)
]