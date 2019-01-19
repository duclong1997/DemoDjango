from django.urls import path
from . import views

urlpatterns = [
      path('showdetail/', views.showDetail),
      path('showListdetail/',views.showList),
      #  get parameter in link <a>
      path('<int:id>/', views.showPost),
]