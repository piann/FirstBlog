from django.urls import path

from . import views

urlpatterns = [
   path('',views.postGate, name='postGate'),
   path('new/',views.postNew, name='postNew'),
]
