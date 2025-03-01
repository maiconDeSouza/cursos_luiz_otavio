from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<slug:slug>', views.recipe, name='recipe'),
    path('category/<str:name>', views.category, name='category'),
]
