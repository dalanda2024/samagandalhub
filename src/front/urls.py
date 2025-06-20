from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import dashboard_utilisateur
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_superuser

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    # cours,dtailcours et formateurs
    # path('courses/<slug:slug>/', views.courses, name='courses'),
    # path('courses/', views.courses, name='courses'),  
    # path('courses/<slug:slug>/', views.course_detail, name='course_detail'),  
    path('trainers/<str:username>/', views.trainer_profile, name='trainer_profile'), 
    path('trainers', views.trainers, name='trainers'), 
    path('profile', views.profile, name='profile'), 
    path('valider_paiement', views.valider_paiement, name='valider_paiement'), 

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # 🔐 Mot de passe oublié et réinitialisation
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

    # Tes vues personnalisées pour l'administrateur
    path('dashboard/', login_required(user_passes_test(is_admin)(views.admin_dashboard)), name='admin_dashboard'),
    path('dashboard/utilisateurs/', views.admin_utilisateurs, name='admin_utilisateurs'),
    path('dashboard/cours/', views.admin_cours, name='admin_cours'),
    path('dashboard/cours/ajouter/', views.admin_ajouter_cours, name='admin_ajouter_cours'),
    path('dashboard/cours/<int:pk>/', views.admin_cours_detail, name='admin_cours_detail'),
    path('dashboard/evenements/', views.admin_evenements, name='admin_evenements'),
    path('dashboard/evenements/ajouter/', views.admin_ajouter_evenement, name='admin_ajouter_evenement'),
    path('dashboard/formateurs/ajouter/', views.admin_ajouter_formateur, name='admin_ajouter_formateur'),
    path('dashboard/modules/ajouter/', views.admin_ajouter_module, name='admin_ajouter_module'),
    # supprimer et modiier cours
    path('dashboard/<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('dashboard/<int:pk>/delete/', views.course_delete, name='course_delete'),

    # utilisateurs
    path('dashboard_utilisateur/', dashboard_utilisateur, name='dashboard_utilisateur'),

    # Cours
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),

    # Modules
    path('module/<int:pk>/', views.voir_module, name='voir_module'),
    path('module/<int:pk>/terminer/', views.marquer_termine, name='marquer_termine'),

    # Quiz
    path('module/<int:module_id>/quiz/', views.quiz_module, name='quiz_module'),



]


