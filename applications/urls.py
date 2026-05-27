from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("add/", views.add_application, name="add_application"),
    path("applications/",  views.application_list, name="application_list"),
    path("applications/<int:id>/", views.application_detail, name="application_detail"),
    path("applications/<int:id>/edit/", views.edit_application, name="edit_application"),
    path(
        "applications/<int:id>/delete/",
        views.delete_application,
        name="delete_application"
    ),

]