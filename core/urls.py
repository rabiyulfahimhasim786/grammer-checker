from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    #path('chekcer/', views.grammer, name='grammer'),
    path('grammer/', views.grammerform, name='grammerform')
]
