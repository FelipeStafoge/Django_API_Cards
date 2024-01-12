from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('take_a_card/', views.take_a_card, name='take_a_card'),
    path('last_three_cards/', views.last_three_cards, name='last_three_cards')
]
