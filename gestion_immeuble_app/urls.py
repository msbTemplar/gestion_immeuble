"""
URL configuration for gestion_immeuble project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

#https://www.youtube.com/watch?v=CdtQSiC8ZNQ

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('enregistrer_charge/', views.enregistrer_charge_view, name='enregistrer_charge'),
    path('liste_des_charges', views.liste_des_charges, name='liste_des_charges'),
    path('actualiser_la_charge/<id_charge>', views.actualiser_la_charge, name='actualiser_la_charge'),
    path('eliminer_la_charge/<id_charge>', views.eliminer_la_charge, name='eliminer_la_charge'),
    path('liste_des_formulaire_charges', views.liste_des_formulaire_charges, name='liste_des_formulaire_charges'),
    path('enregistrer_formulaire_charge/', views.enregistrer_formulaire_charge_view, name='enregistrer_formulaire_charge'),
    path('actualiser_formulaire_charge/<id_formulaire_charge>', views.actualiser_formulaire_charge, name='actualiser_formulaire_charge'),
    path('eliminer_formulaire_charge/<id_formulaire_charge>', views.eliminer_formulaire_charge, name='eliminer_formulaire_charge'),
    path('liste_des_formulaire_liste_proprietaires', views.liste_des_formulaire_liste_proprietaires, name='liste_des_formulaire_liste_proprietaires'),
    path('enregistrer_formulaire_liste_proprietaire/', views.enregistrer_formulaire_liste_proprietaire_view, name='enregistrer_formulaire_liste_proprietaire'),
    path('actualiser_formulaire_liste_proprietaires/<id_formulaire_liste_proprietaire>', views.actualiser_formulaire_liste_proprietaires, name='actualiser_formulaire_liste_proprietaires'),
    path('eliminer_formulaire_liste_proprietaires/<id_formulaire_liste_proprietaire>', views.eliminer_formulaire_liste_proprietaires, name='eliminer_formulaire_liste_proprietaires'),
    path('liste_formulaire_cotization', views.liste_formulaire_cotization, name='liste_formulaire_cotization'),
    path('get_proprietaire_data/<int:pk>/', views.get_proprietaire_data, name='get_proprietaire_data'),
    path('enregistrer_formulaire_cotization/', views.enregistrer_formulaire_cotization_view, name='enregistrer_formulaire_cotization'),
    path('actualiser_formulaire_cotization/<id_formulaire_cotization>', views.actualiser_formulaire_cotization, name='actualiser_formulaire_cotization'),
    path('eliminer_formulaire_cotization/<id_formulaire_cotization>', views.eliminer_formulaire_cotization, name='eliminer_formulaire_cotization'),
    path('get_last_id/', views.get_last_id, name='get_last_id'),
    path('liste_situation_caisse', views.liste_situation_caisse, name='liste_situation_caisse'),
    path('liste_formulaire_p_concierge', views.liste_formulaire_p_concierge, name='liste_formulaire_p_concierge'),
    path('enregistrer_formulaire_p_concierge/', views.enregistrer_formulaire_p_concierge_view, name='enregistrer_formulaire_p_concierge'),
    path('actualiser_formulaire_p_concierge/<id_formulaire_p_concierge>', views.actualiser_formulaire_p_concierge, name='actualiser_formulaire_p_concierge'),
    path('eliminer_formulaire_p_concierge/<id_formulaire_p_concierge>', views.eliminer_formulaire_p_concierge, name='eliminer_formulaire_p_concierge'),
    path('formulaire_cotization_pdf/', views.formulaire_cotization_pdf, name='formulaire_cotization_pdf'),
    path('formulaire_cotization_pdf/<int:id_formulaire_cotization>/', views.formulaire_cotization_pdf, name='formulaire_cotization_pdf'),
    path('generate_temp_pdf/', views.generate_temp_pdf, name='generate_temp_pdf'),
    path('serve_temp_pdf/<str:filename>/', views.serve_temp_pdf, name='serve_temp_pdf'),
    path('formulaire_p_concierge_pdf/<int:id_formulaire_p_concierge>/', views.formulaire_p_concierge_pdf, name='formulaire_p_concierge_pdf'),
    path('generate_p_concierge_temp_pdf/', views.generate_p_concierge_temp_pdf, name='generate_p_concierge_temp_pdf'),
    path('serve_p_concierge_temp_pdf/<str:filename>/', views.serve_p_concierge_temp_pdf, name='serve_p_concierge_temp_pdf'),
    path('backup/', views.backup_database, name='backup_database'),



]
