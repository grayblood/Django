from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('fraseRandom', views.fraseRandom, name="fraseRandom"),
    path('fraseRandomSFW', views.fraseRandomSFW, name="fraseRandomSFW"),
    path('frasesDe/<str:nom>', views.fraseNom, name="fraseNom"),
    path('addFrase/', views.addfrase, name="addfrase"),
    path('buscar/<int:frase_id>/', views.detail, name="detail"),
    path('addTag/<int:frase_id>/<str:nomTag>/', views.addTag, name="addTag"),
    path('removeTag/<int:frase_id>/<str:nomTag>/', views.removeTag, name="removeTag"),

]
