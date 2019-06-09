from django.urls import path

from . import views

app_name = 'cards'
urlpatterns = [
    # ex: /cards/
    path('', views.index, name='index'),
    # ex: /cards/5/
    path('<int:card_id>/', views.show, name='show'),
]